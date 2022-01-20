from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('signin', views.signinview, name='signinview'),
    path('signup', views.signup, name='signupview'),
]