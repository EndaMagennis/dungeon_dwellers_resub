from django.db import models
from profiles.models import User
from products.models import Product

# Create your models here.
class Wishlist(models.Model):
    """Model for user wishlist"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='wishlist'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False    
    )    
    class Meta:
        """Meta class for Wishlist"""
        ordering = ['-created_at']
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        """String representation of Wishlist"""
        return f'{self.user.username}\'s wishlist'
    
    def add_to_wishlist(self, product):
        """Method to add product to wishlist"""
        if product not in self.products.all():
            self.products.add(product)
            return True
        return False
    
    def remove_from_wishlist(self, product):
        """Method to remove product from wishlist"""
        if product in self.products.all():
            self.products.remove(product)
            return True
        return False
    
    def clear_wishlist(self):
        """Method to clear wishlist"""
        self.products.clear()
        return True
    
    def get_products(self):
        """Method to get product from wishlist"""
        return self.products.all()
