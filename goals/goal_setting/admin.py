from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'time_create', 'image', 'is_published']
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'time_create')


admin.site.register(News, NewsAdmin)
