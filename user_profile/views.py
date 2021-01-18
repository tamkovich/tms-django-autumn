from django.contrib.auth.models import User
from django.shortcuts import render


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "user/profile.html", {"user": user})
