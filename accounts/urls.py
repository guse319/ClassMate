from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    # Account creation
    path('signup/', views.signupuser, name='signupuser'),
    path('signup/tutor/', views.tutor, name='tutor'),
    path('signup/teacher/', views.teacher, name='teacher'),
    path('signup/student/', views.student, name='student'),
    path('signup/parent/', views.parent, name='parent'),

    # Authentication
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
