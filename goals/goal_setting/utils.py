from .models import *


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        news = News.objects.all()
        context['news'] = news
        return context
