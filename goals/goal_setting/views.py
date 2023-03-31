import datetime

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CreateGoalsForm, FormSendMessage, RegisterUserForm, LoginUserForm
from .texts import g_info, prv_policy, user_agreement
from .utils import *


def index(request):
    return render(request, 'goal_setting/index.html', context={
        'title': 'Sprout | Лучшее приложение для достижения целей!'
    })


def goals_info(request):
    return render(request, 'goal_setting/goals_info.html',
                  context={'title': 'Sprout | Как ставить цели', 'g_info': g_info})


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


class ListNews(DataMixin, ListView):
    model = News
    template_name = 'goal_setting/news.html'
    context_object_name = 'news_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sprout | Новости успехов!')
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


def privacy_policy(request):
    return render(request, 'goal_setting/privacy_policy.html',
                  context={'title': 'Sprout | Политика конфиденциальности', 'prv_policy': prv_policy})


def condition_of_use(request):
    return render(request, 'goal_setting/condition_of_use.html',
                  context={'title': 'Sprout | Условия пользования', 'user_agreement': user_agreement})


def send_message(request):
    form = FormSendMessage()

    if request.method == 'POST':
        form = FormSendMessage(request.POST)
        if form.is_valid:

            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            data = f'Имя пользователя: {name}<br> Email: {email}<br> Сообщение: {message}'
            msg = EmailMultiAlternatives(subject='SPROUT', to=['vk.ryzhenkov@gmail.com', ])
            msg.attach_alternative(data, 'text/html')
            msg.send()
            return redirect('home')
        else:
            form = FormSendMessage()
    return render(request, 'goal_setting/contact.html', context={'title': 'Sprout | Обратная связь', 'form': form})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'goal_setting/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sprout | Регистрация пользователя'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'goal_setting/login.html'
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sprout | Авторизация'
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
