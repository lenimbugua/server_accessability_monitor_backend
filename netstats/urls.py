from django.urls import path
from . import views

urlpatterns = [
    path('net_stats/', views.StatsList.as_view()),
    path('net_stats/<int:pk>/', views.StatsDetail.as_view()),
    path('files/', views.FilePathList.as_view()),
]
