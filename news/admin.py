from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'publish_date']
    list_filter = ['publish_date']

    title = 'Название новости'

admin.site.register(News, NewsAdmin)
