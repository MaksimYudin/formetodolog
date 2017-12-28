from django.http import HttpResponse
from django.shortcuts import render

def news(request):
    return render(request, 'news/news.html')
