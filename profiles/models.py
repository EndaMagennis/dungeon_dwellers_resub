from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

from django_countries.fields import CountryField


class Profile(models.Model):
    """Model for user profile"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Last Name',
    )
    avatar = CloudinaryField(
        'avatar',
        folder='dungeon_avatars',
        blank=True,
        null=True,
        eager=[
            {'width': '50', 'height': '50', 'crop': 'crop'}  # noqa
        ],
        transformation={
            'width': '500', 'height': '500', 'crop': 'fill'  # noqa
        }
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return self.first_name
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return 'static/images/default_pfp.jpg'


class Address(models.Model):
    """Model for user address"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
        default='',
        verbose_name='User',
    )
    address_line_1 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='Address 1',
    )
    address_line_2 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='Address 2',
    )
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='County',
    )
    city = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='City',
    )
    country = CountryField(
        blank_label='(select country)',
        null=True,
        blank=True,
        verbose_name='Country',
    )
    post_code = models.CharField(
        max_length=10,
        verbose_name='Post Code',
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Phone Number',
    )
    is_default = models.BooleanField(
        default=False,
        verbose_name='Default Address',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
    )

    def __str__(self):
        return f'{self.address_line_1}, {self.city}, {self.country} {self.post_code}'  # noqa

    def save(self, *args, **kwargs):
        """Set default address to False if another address is set to True"""
        super().save(*args, **kwargs)

        if self.is_default:
            for address in self.user.addresses.exclude(id=self.id):
                address.is_default = False
                address.save()
