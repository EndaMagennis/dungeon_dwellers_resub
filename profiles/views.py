from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Profile, Address
from .forms import ProfileForm, AddressForm

class ProfileView(View):
    """View for user profile"""
    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=request.user)
            addresses = Address.objects.filter(user=request.user)
            default_address = addresses.filter(is_default=True)

            context = {
                'profile': profile,
                'addresses': addresses,
                'default_address': default_address,
            }
            return render(request, 'profiles/profile.html', context)
        else:
            return render(request, 'home/index.html')


class EditAvatarAjaxView(View):
    """View for editing user avatar"""

    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            avatar = request.FILES.get('avatar')
            profile = get_object_or_404(Profile, user=request.user)
            profile.avatar = avatar
            profile.save()
            return redirect(reverse('profile', args=[request.user.username]))
    

class ProfileUpdateView(View):
    """View for updating user profile"""
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(instance=profile)

        address_form = AddressForm()
        context = {
            'profile_form': profile_form,
            'address_form': address_form,
        }
        return render(request, 'profiles/update_profile.html', context)
    
    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        address_form = AddressForm(request.POST)

        if profile_form.is_valid() and address_form.is_valid():
            address = address_form.save(commit=False)
            address.user = request.user
            address.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            messages.success(request, 'Address created successfully')
            return redirect(reverse('profile', args=[request.user.username]))
        context = {
            'profile': profile,
            'address': address
        }
        return render(request, 'profiles/profile.html', context)
    

class AddressCreateView(View):
    """View for creating user address"""
    def get(self, request, *args, **kwargs):
        form = AddressForm()
        context = {
            'form': form,
        }
        return render(request, 'profiles/add_address.html', context)
    
    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'Address created successfully')
            return redirect(reverse('profile', args=[request.user.username]))
        context = {
            'form': form,
        }
        return render(request, 'profiles/profile.html', context)