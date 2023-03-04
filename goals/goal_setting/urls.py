from django.urls import path

from goal_setting.views import *

urlpatterns = [
    path('', index, name='home'),
    path('why_us/', why_us, name='why_us'),
    path('goals_how_it_work/', goals_info, name='goals_info'),
    path('points_how_it_work/', points_info, name='points_info'),
    path('leaders/', show_leaders, name='leaders'),
    path('goals/', CreateGoals.as_view(), name='goals'),
    path('goals/my_goals/', GoalsMenu.as_view(), name='my_goals'),
    path('goals/my_goals/<goal_slug>/', ShowGoal.as_view(), name='goal'),

    # url(r'^delete/(?P<part_id>[0-9]+)/$', view.function, name='delete_view'),
    path(r'^goals/my_goals/(?P<goal_slug>\d+)$', delete_goal, name='delete_goal'),
    # path(r'^delete/(?P<goal_slug>+)/$', delete_goal, name='delete_goal'),

    path('news/', ListNews.as_view(), name='news'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
    path('about/', about_us, name='about'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('condition_of_use/', condition_of_use, name='condition_of_use'),
    path('contact/', contact, name='contact'),
]
