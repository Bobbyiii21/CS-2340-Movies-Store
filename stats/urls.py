from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='stats.index'),
    path('users/', views.users, name='stats.users'),
    path('movies/', views.movies, name='stats.movies'),
    path('users/<int:id>/see_orders/', views.see_orders, name='stats.see_orders'),
]