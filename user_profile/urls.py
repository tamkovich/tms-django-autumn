from django.urls import path

from user_profile import views

urlpatterns = [
    path('<str:username>/', views.profile, name='user-profile'),
    path('<str:username>/edit/', views.edit_profile, name='edit-profile'),
    path('<str:username>/delete/', views.delete_profile, name='delete-profile')
]
