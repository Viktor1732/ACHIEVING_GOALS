from django.shortcuts import render

menu_items = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Цели', 'url_name': 'goals'},
    {'title': 'База знаний', 'url_name': 'info'},
    {'title': 'Обратная связь', 'url_name': 'contact'}
]

menu_auth = [
    {'title': 'Регистрация', 'url_name': 'registration'},
    {'title': 'Вход', 'url_name': 'login'},
]


def index(request):
    return render(request, 'goal_setting/index.html',
                  context={'menu_items': menu_items, 'menu_auth': menu_auth, 'title': 'home'})


def show_goals_menu(request):
    return render(request, 'goal_setting/goals_menu.html',
                  context={'menu_items': menu_items, 'menu_auth': menu_auth, 'title': 'Редактирование целей'})


def show_info(request):
    return render(request, 'goal_setting/info.html',
                  context={'menu_items': menu_items, 'menu_auth': menu_auth, 'title': 'Редактирование целей'})


def contact(request):
    return render(request, 'goal_setting/contact.html',
                  context={'menu_items': menu_items, 'menu_auth': menu_auth, 'title': 'Обратная связь'})


def show_selected_item(request):
    pass


def login(request):
    pass


def registration(request):
    pass
