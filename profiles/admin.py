from django.contrib import admin
from .models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'created_at')
    search_fields = ('user__username', 'first_name', 'last_name')
    ordering = ('user',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line_1', 'city', 'post_code', 'country')
    search_fields = ('user__username', 'address_line_1', 'city', 'post_code', 'country')
    ordering = ('user',)
    list_filter = ('country',)