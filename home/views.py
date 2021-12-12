from django.shortcuts import render, redirect, Http404, get_object_or_404
from .models import Article
from django.views.generic.base import TemplateView


def home(request):
    return render(request, 'home/home.html', {})

def actuality(request):

        article = Article.objects.all()

        context = {'article': article}
        return render(request, 'home/actuality.html', context)

class PageView(TemplateView):
    pass


def pageArticle(request, pk):

        article = Article.objects.get(id=pk)

        context = {'article': article}
        return render(request, 'home/page_articles.html', context)



def error_404_view(request, exception):

    return render(request, 'home/home.html', {}, status=404)


def handle_server_error(request):

    return render(request, 'home/home.html', {}, status=505)