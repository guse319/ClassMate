from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [

    # profile
    path('', views.profile, name='profile'),

    # New profile
    path('create_user/', views.create_user, name='create_user'),
    path('create', views.create, name='create'),
]
