from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [

    # profile
    path('', views.profile, name='profile'),
    path('<int:user_id>/', views.viewprofile, name='viewprofile'),

    # New profile
    path('create_user/', views.create_user, name='create_user'),
    path('create/', views.create, name='create'),

    # Search
    path('search/', views.search, name='search'),
]
