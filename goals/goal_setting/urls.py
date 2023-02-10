from django.urls import path

from goal_setting.views import *

urlpatterns = [
    path('', index, name='home'),
    path('goals_menu/', show_goals_menu, name='goals'),
    path('info/', show_info, name='info'),
    path('contact/', contact, name='contact'),
]
