from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('add/', views.add, name='addPost'),
    path('<str:post_slug>', views.details, name='postView'),
    path('edit/<int:post_id>/', views.edit, name='editPost'),
]