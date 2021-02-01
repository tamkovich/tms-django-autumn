from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination

from api.pagination import CustomPageNumberPagination
from api.permissions import IsAuthorOrReadOnly
from home.models import Article
from api.serializers import ArticleSerializer, UserSerializer


class ArticleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPageNumberPagination


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    pagination_class = LimitOffsetPagination
