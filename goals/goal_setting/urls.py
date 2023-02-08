from django.urls import path

from goal_setting.views import *

urlpatterns = [
    path('', index, name='home')
]
