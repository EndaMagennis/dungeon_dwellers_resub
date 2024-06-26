from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import Profile, Address
from profiles.forms import ProfileForm, AddressForm
from bag.contexts import bag_contents

from checkout.webhook_handler import StripeWH_Handler
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'post_code': request.POST['post_code'],
            'city': request.POST['city'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():  # noqa
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products was not found. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]
                ))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                address = Address.objects.get(
                    user=request.user, is_default=True
                )
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': address.phone_number,
                    'country': address.country,
                    'post_code': address.post_code,
                    'city': address.city,
                    'address_line_1': address.address_line_1,
                    'address_line_2': address.address_line_2,
                    'county': address.county,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
            except Address.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    handler = StripeWH_Handler(request)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        address = Address.objects.get(user=request.user, is_default=True)
        # Attach the user's profile to the order
        order.profile = profile
        order.save()

        # Save the user's info
        if save_info:
            data = {
                'phone_number': order.phone_number,
                'country': order.country,
                'post_code': order.post_code,
                'city': order.city,
                'address_line_1': order.address_line_1,
                'address_line_2': order.address_line_2,
                'county': order.county,
            }
            user_address_form = AddressForm(data, instance=address)
            user_profile_form = ProfileForm(data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
            if user_address_form.is_valid():
                updated_address = user_address_form.save(commit=False)
                updated_address.is_default = True
                updated_address.save()
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    handler._send_confirmation_email(order)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/order_history.html'

    context = {
        'order': order
    }

    return render(request, template, context)
