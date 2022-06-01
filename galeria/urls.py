from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('manage/', views.manage, name='manage'),
     path('search/', views.search_results, name='search_results')
]
