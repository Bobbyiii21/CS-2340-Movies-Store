from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='map.index'),
    path('api/regional-stats/', views.regional_stats, name='map.regional_stats'),
]