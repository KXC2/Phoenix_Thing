from django.urls import path, re_path
from . import views

app_name = 'Personal'

urlpatterns = [
path('', views.user_login, name='login'),
path('authenticate_user/', views.authenticate_user,
name='authenticate_user'),
path('account_creation/', views.account_creation, name = "account_creation"),
path('PhoenixDiary/Personal', views.phoenixDiary, name = "phoenixDiary"),
path('puns/Personal', views.jokes, name = "jokes"),
path('thoughts/Personal', views.thoughts, name = "thoughts")
]
