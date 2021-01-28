from django.urls import path

from api import views

urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view()),
    path(
        'articles/<int:pk>/',
        views.ArticleDetailAPIView.as_view(),
        name='api-one-article'
    ),
    path('users/', views.UserListAPIView.as_view(), name='api-users'),
    path(
        'users/<str:username>/',
        views.UserDetailAPIView.as_view(),
        name='api-one-user'
    ),
]
