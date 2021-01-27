from django.urls import path

from api import views

urlpatterns = [
    path('test/', views.test),
    path('articles/', views.ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', views.get_article),
    # path('<str:username>/', views.UserDetailView.as_view(), name='user-profile'),
    # path('<str:username>/edit/', views.UserUpdateView.as_view(), name='edit-profile'),
    # path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete-profile')
]
