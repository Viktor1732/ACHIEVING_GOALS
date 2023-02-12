from django.shortcuts import render


def index(request):
    return render(request, 'goal_setting/index.html', context={'title': 'Лучшее приложение для достижения целей!'})


def why_us(request):
    return render(request, 'goal_setting/why_us.html', context={'title': 'Почему Мы?'})


def goals_info(request):
    return render(request, 'goal_setting/goals_info.html', context={'title': 'Информация о целях'})


def points_info(request):
    return render(request, 'goal_setting/points_info.html', context={'title': 'Информация о баллах'})


def show_all_goals(request):
    return render(request, 'goal_setting/goals.html', context={'title': 'Последние опубликованные цели'})


def show_news(request):
    return render(request, 'goal_setting/news.html', context={'title': 'Новости'})


def about_us(request):
    return render(request, 'goal_setting/about.html', context={'title': 'О нас'})


def show_leaders(request):
    return render(request, 'goal_setting/leader_board.html', context={'title': 'Наши лидеры'})


def privacy_policy(request):
    return render(request, 'goal_setting/privacy_policy.html', context={'title': 'Политика конфиденциальности'})


def condition_of_use(request):
    return render(request, 'goal_setting/condition_of_use.html', context={'title': 'Условия пользования'})


def contact(request):
    return render(request, 'goal_setting/contact.html', context={'title': 'Обратная связь'})
