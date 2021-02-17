from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.urls import reverse
from rest_framework import serializers

from home.models import Article
from user_profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["country", "phone", "birth_date"]


class ArticleSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ["id", "title", "content", "author", "link", "image"]

    def get_link(self, obj):
        uri = reverse("articles-detail", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated and instance.author_id == user.id:
            return super(ArticleSerializer, self).update(instance, validated_data)
        raise Exception("No credentials")


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "articles",
            "link",
            "profile",
        ]

    def get_articles(self, obj):
        articles = Article.objects.filter(author=obj)
        s = ArticleSerializer(articles, many=True, context=self.context)
        return s.data

    def get_link(self, obj):
        uri = reverse("users-detail", kwargs={"username": obj.username})
        return self.context["request"].build_absolute_uri(uri)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def create(self, validated_data):
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password == password2:
            user = User.objects.create_user(
                username=validated_data["username"], email=validated_data["email"]
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({"password": "Password are not the same"})
