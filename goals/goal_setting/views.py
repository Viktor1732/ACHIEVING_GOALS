from django.shortcuts import render


def index(request):
    return render(request, 'goal_setting/index.html', context={'title': 'Лучшее приложение для достижения целей!'})
