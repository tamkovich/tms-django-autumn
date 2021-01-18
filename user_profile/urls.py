from django.urls import path

from user_profile import views

urlpatterns = [
    path('<str:username>/', views.profile, name='user-profile'),
]
