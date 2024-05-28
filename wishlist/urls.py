from django.urls import path
from .views import(
    WishlistView, AddRemoveWishlistView
)

urlpatterns = [
    path('', WishlistView.as_view(), name='wishlist'),
    path('add_remove/', AddRemoveWishlistView.as_view(), name='add_remove_wishlist'),
]