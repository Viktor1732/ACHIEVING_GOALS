from django.shortcuts import render

menu_items = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Цели', 'url_name': 'goal'},
    {'title': 'Архив', 'url_name': 'archive'},
    {'title': 'База знаний', 'url_name': 'info'},
]

menu_auth = [
    {'title': 'Регистрация', 'url_name': 'registration'},
    {'title': 'Вход', 'url_name': 'login'},
]


def index(request):
    return render(request, 'goal_setting/index.html',
                  context={'menu_items': menu_items, 'menu_auth': menu_auth, 'title': 'home'})
