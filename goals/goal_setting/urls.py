from django.urls import path

from goal_setting.views import index

urlpatterns = [
    path('', index, name='home')
]
