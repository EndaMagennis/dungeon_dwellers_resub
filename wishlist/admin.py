from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin class for Wishlist"""
    list_display = ('user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'products')
        }),
        ('Created at', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    filter_horizontal = ('products',)
    actions = ['clear_wishlist']

    def clear_wishlist(self, request, queryset):
        """Action to clear wishlist"""
        for wishlist in queryset:
            wishlist.clear_wishlist()
        self.message_user(request, 'Wishlist cleared')
    clear_wishlist.short_description = 'Clear selected wishlists'
