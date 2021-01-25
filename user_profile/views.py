from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from user_profile.models import Profile


from django.views.generic import DetailView, DeleteView, UpdateView


class UserDetailView(DetailView):
    model = User
    template_name = "user/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"


class UserUpdateView(UpdateView):
    model = User
    template_name = "user/edit_profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"


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


class UserDeleteView(DeleteView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "user/delete_profile.html"
    success_url = "/articles/"
    context_object_name = "user"
