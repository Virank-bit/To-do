from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login1, name="login"),
    path('todo', views.TOdo, name="todo"),
    path('delete_todo/<int:srno>', views.delete_todo),
]