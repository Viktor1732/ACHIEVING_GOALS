import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import CreateGoalsForm
from .utils import *


def index(request):
    return render(request, 'goal_setting/index.html', context={'title': 'Лучшее приложение для достижения целей!'})


def why_us(request):
    return render(request, 'goal_setting/why_us.html', context={'title': 'Sprout | Почему Мы?'})


def goals_info(request):
    return render(request, 'goal_setting/goals_info.html', context={'title': 'Информация о целях'})


class CreateGoals(DataMixin, CreateView):
    form_class = CreateGoalsForm
    template_name = 'goal_setting/goals.html'
    success_url = reverse_lazy('goals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.all()[:3]
        list_goals = Goals.objects.all()

        def count_goals_act():
            if list_goals.filter(is_completed=False).count() > 0:
                return list_goals.filter(is_completed=False).order_by('-time_of_create')[:5]
            else:
                return None

        def count_goals_arc():
            if list_goals.filter(is_completed=True).count() > 0:
                return list_goals.filter(is_completed=True).order_by('-time_of_create')[:5]
            else:
                return None

        c_def = self.get_user_context(title='Sprout | Работа с целями', news_list=news,
                                      list_goals_act=count_goals_act(),
                                      list_goals_arc=count_goals_arc())
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class GoalsMenu(DataMixin, ListView):
    model = Goals
    template_name = 'goal_setting/goals-menu.html'
    context_object_name = 'goals_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        def get_period_goals():
            list_goals_less_90_days = []
            list_goals_from_3_to_12_months = []
            list_goals_from_1_to_3_years = []
            list_goals_more_3_years = []

            for goal in Goals.objects.all():
                period = goal.time_of_end - goal.time_of_create
                if period < datetime.timedelta(days=90):
                    list_goals_less_90_days.append(goal.title)
                elif datetime.timedelta(days=90) < period < datetime.timedelta(days=365):
                    list_goals_from_3_to_12_months.append(goal.title)
                elif datetime.timedelta(days=365) < period < datetime.timedelta(days=1095):
                    list_goals_from_1_to_3_years.append(goal.title)
                else:
                    list_goals_more_3_years.append(goal.title)

            return {
                'less_90_days': list_goals_less_90_days,
                'from_3_to_12_months': list_goals_from_3_to_12_months,
                'from_1_to_3_years': list_goals_from_1_to_3_years,
                'more_3_years': list_goals_more_3_years
            }

        c_def = self.get_user_context(title='Sprout | Мои цели', period=get_period_goals())
        return dict(list(context.items()) + list(c_def.items()))


def points_info(request):
    return render(request, 'goal_setting/points_info.html', context={'title': 'Информация о баллах'})


def show_leaders(request):
    return render(request, 'goal_setting/leader_board.html', context={'title': 'Наши лидеры'})


class ListNews(DataMixin, ListView):
    model = News
    template_name = 'goal_setting/news.html'
    context_object_name = 'news_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Новости успехов!')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ShowNews(DataMixin, DetailView):
    model = News
    template_name = 'goal_setting/show_news.html'
    context_object_name = 'news_list'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = News.objects.get(slug=self.kwargs['news_slug'])
        c_def = self.get_user_context(title=str(c.title))
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
