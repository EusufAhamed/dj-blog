from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signupview'),
    path('signin/', views.signin, name='signinview'),
    path('<str:username>', views.profile, name='profileview'),
    path('<str:username>/settings/', views.profile_update, name='profileUpdateView'),
    path('logout/', views.loginout, name='logoutview'),
]