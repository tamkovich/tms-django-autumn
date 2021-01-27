from django.http import JsonResponse

from home.models import Article
from api.serializers import ArticleSerializer

from rest_framework.generics import ListAPIView


def test(request):
    return JsonResponse(
        {
            "date": "2020-27-01",
            "group": "Z38",
        }
    )


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def all_articles(request):
    articles = Article.objects.all()
    s = ArticleSerializer(articles, many=True)
    return JsonResponse(s.data, safe=False)


def get_article(request, pk):
    article = Article.objects.filter(pk=pk)
    s = ArticleSerializer(article)
    return JsonResponse(s.data)
