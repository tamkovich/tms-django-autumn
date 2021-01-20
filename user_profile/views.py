from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from user_profile.models import Profile


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "user/profile.html", {"user": user})


def edit_profile(request, username):
    print(request.POST)
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.phone = request.POST.get('phone')
        profile.country = request.POST.get('country')
        user.save()
        profile.save()
    return render(request, "user/edit_profile.html", {"user": user})


def delete_profile(request, username):
    """
    Фукнция удаляет пользователя при запросе POST,
    и возвращает кнокпу на удаление пользователя при GET
    """
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.delete()
        return render(request, "user/successfully_delete_profile.html")
    return render(request, "user/delete_profile.html", {"user": user})
