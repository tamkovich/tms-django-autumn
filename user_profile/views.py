from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "user/profile.html", {"user": user})


def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "user/edit_profile.html", {"user": user})
