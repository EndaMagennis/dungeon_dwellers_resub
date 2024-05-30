from django.urls import path
from .views import(
    ProfileView, ProfileUpdateView,
    EditAvatarAjaxView
) 


urlpatterns = [
    path('<str:user>/', ProfileView.as_view(), name='profile'),
    path('<str:user>/update', ProfileUpdateView.as_view(), name='update_profile'),
    path('profile/edit_avatar/', EditAvatarAjaxView.as_view(), name='edit_avatar'),
]
