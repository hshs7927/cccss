from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allmenu/', views.allmenu, name='allmenu'),
    path('allmenu/<str:biz_url>', views.test, name='test')
]