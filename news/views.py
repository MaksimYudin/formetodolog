from django.http import HttpResponse
from django.shortcuts import render
from .models import News
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def news(request):
    news_list = News.objects.all()
    #current_page = Paginator(article_list, 2)
    context = {
        'news_list': news_list,
        'user_name': auth.get_user(request).username
    }
    return render(request, 'news/news.html', context)

@login_required
def news_detail(request, news_id):
    news_detail = News.objects.get(id=news_id)
    context = {
        'news_detail': news_detail,
        'user_name': auth.get_user(request).username
    }
    return render(request, 'news/new_detail.html', context)
