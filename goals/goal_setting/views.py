import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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
    template_name = 'goal_setting/create_goal.html'
    success_url = reverse_lazy('goals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sprout | Работа с целями')
        return dict(list(context.items()) + list(c_def.items()))


class GoalsMenu(DataMixin, ListView):
    model = Goals
    template_name = 'goal_setting/goals.html'
    context_object_name = 'goals_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.all()[:6]

        def get_period_goals():
            list_goals_less_90_days = []
            list_goals_from_3_to_12_months = []
            list_goals_from_1_to_3_years = []
            list_goals_more_3_years = []

            for goal in Goals.objects.filter(is_completed=False):
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

        c_def = self.get_user_context(title='Sprout | Мои цели', period=get_period_goals(), news_list=news)
        return dict(list(context.items()) + list(c_def.items()))


class ShowGoal(DataMixin, DetailView):
    model = Goals
    template_name = 'goal_setting/show_goal.html'
    context_object_name = 'goal'
    slug_url_kwarg = 'goal_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sprout | goal: ' + str(context['goal']))
        return dict(list(context.items()) + list(c_def.items()))


def delete_goal(request, goal_slug=None):
    Goals.objects.get(slug=goal_slug).delete()
    return redirect('goals')


def completing_goal(request, goal_slug=None):
    goal = Goals.objects.get(slug=goal_slug)
    goal.is_completed = True
    goal.save()
    return redirect('goals')


class GoalUpdate(DataMixin, UpdateView):
    model = Goals
    form_class = CreateGoalsForm
    template_name = 'goal_setting/update_goal.html'
    context_object_name = 'form'
    slug_url_kwarg = 'goal_slug'
    success_url = reverse_lazy('goals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sprout | Изменить цель')
        return dict(list(context.items()) + list(c_def.items()))


class ArchiveMenu(DataMixin, ListView):
    model = Goals
    template_name = 'goal_setting/show-archive.html'
    context_object_name = 'goals_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.all()[:6]

        def get_period_goals():
            list_goals_less_90_days = []
            list_goals_from_3_to_12_months = []
            list_goals_from_1_to_3_years = []
            list_goals_more_3_years = []

            for goal in Goals.objects.filter(is_completed=True):
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

        c_def = self.get_user_context(title='Sprout | Архив', period=get_period_goals(), news_list=news)
        return dict(list(context.items()) + list(c_def.items()))


def cancel_archive(request, goal_slug):
    goal = Goals.objects.get(slug=goal_slug)
    goal.is_completed = False
    goal.save()
    return redirect('archive')


def delete_goal_archive(request, goal_slug=None):
    Goals.objects.get(slug=goal_slug).delete()
    return redirect('archive')


class PublicGoals(DataMixin, ListView):
    model = Goals
    template_name = 'goal_setting/public_goals.html'
    context_object_name = 'list_goals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sprout | Публичные цели всех пользователей')
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
