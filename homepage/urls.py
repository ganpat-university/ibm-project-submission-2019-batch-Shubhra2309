from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView, name='about'),
    path('login/', views.Login, name='login'),
]