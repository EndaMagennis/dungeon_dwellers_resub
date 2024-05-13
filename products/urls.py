from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductAddView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductAddView.as_view(), name='add_product')
]