from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductAddView,
    ProductEditView,
    ProductDeleteView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductAddView.as_view(), name='add_product'),
    path('edit/<int:product_id>/', ProductEditView.as_view(), name='edit_product'),
    path('delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete_product')
]