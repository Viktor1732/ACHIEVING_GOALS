from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'time_create', 'image', 'is_published']
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'time_create')


class GoalsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'time_of_create', 'time_of_end', 'privacy', 'is_completed']
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('is_completed', 'time_of_create')


admin.site.register(News, NewsAdmin)
admin.site.register(Goals, GoalsAdmin)
