from django.urls import path

from goal_setting.views import *

urlpatterns = [
    path('', index, name='home'),
    path('goals_how_it_work/', goals_info, name='goals_info'),
    path('goals/create_goal', CreateGoals.as_view(), name='create_goal'),
    path('goals/', GoalsMenu.as_view(), name='goals'),
    path('goals/show_goal/<goal_slug>/', ShowGoal.as_view(), name='goal'),
    path(r'^goals/show_goal/(?P<goal_slug>\d+)$', delete_goal, name='delete_goal'),
    path(r'goals/show_goal/<goal_slug>', completing_goal, name='completing_goal'),
    path('goals/update/<slug:goal_slug>/', GoalUpdate.as_view(), name='update_goal'),
    path('archive/', ArchiveMenu.as_view(), name='archive'),
    path('archive/<goal_slug>', cancel_archive, name='cancel_archive'),
    path(r'^archive/(?P<goal_slug>\d+)$', delete_goal_archive, name='delete_goal_archive'),
    path('public_goals', PublicGoals.as_view(), name='public_goals'),
    path('news/', ListNews.as_view(), name='news'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('condition_of_use/', condition_of_use, name='condition_of_use'),
    path('contact/', send_message, name='contact'),
    path('registration/', RegisterUser.as_view(), name='register'),
    path('authentication/', LoginUser.as_view(), name='auth'),
    path('logout/', logout_user, name='logout'),
]
