from django.shortcuts import render
from django.views.generic import ListView

from .utils import *


def index(request):
    return render(request, 'goal_setting/index.html', context={'title': 'Лучшее приложение для достижения целей!'})


def why_us(request):
    return render(request, 'goal_setting/why_us.html', context={'title': 'Sprout | Почему Мы?'})


def goals_info(request):
    return render(request, 'goal_setting/goals_info.html', context={'title': 'Информация о целях'})


def points_info(request):
    return render(request, 'goal_setting/points_info.html', context={'title': 'Информация о баллах'})


def show_all_goals(request):
    return render(request, 'goal_setting/goals.html', context={'title': 'Последние опубликованные цели'})


def show_leaders(request):
    return render(request, 'goal_setting/leader_board.html', context={'title': 'Наши лидеры'})


class ShowNews(DataMixin, ListView):
    model = News
    template_name = 'goal_setting/news.html'
    context_object_name = 'news_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Новости успехов!')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


def about_us(request):
    return render(request, 'goal_setting/about.html', context={'title': 'О нас'})


def privacy_policy(request):
    return render(request, 'goal_setting/privacy_policy.html', context={'title': 'Политика конфиденциальности'})


def condition_of_use(request):
    return render(request, 'goal_setting/condition_of_use.html', context={'title': 'Условия пользования'})


def contact(request):
    return render(request, 'goal_setting/contact.html', context={'title': 'Обратная связь'})
