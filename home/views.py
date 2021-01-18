from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from home.models import Article


def home(request):
    return HttpResponse("<b>Hello</b> <i>world!</i>")


def markus(request):
    return HttpResponse("Hello Markus!")


def debug(request):
    page = request.GET.get('page')
    return HttpResponse(f"This is Debug URL. Page number {page}")


def user(request, username):
    return HttpResponse(f"This is user {username}")


def all_articles(request):
    print(request.user)
    if request.user.is_authenticated:
        articles = Article.objects.all()
        return render(
            request, "articles.html", {"articles": articles},
        )
    return HttpResponse(f"You are not logged in", 404)


@login_required
def get_article(request, pk: int):
    article = get_object_or_404(Article, pk=pk)
    return render(
        request, "article.html", {"obj": article},
    )
