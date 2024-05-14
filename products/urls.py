from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductAddView,
    ProductImageAddView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductAddView.as_view(), name='add_product'),
    path('add_image/', ProductImageAddView.as_view(), name='add_image')
]