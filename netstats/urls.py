from django.urls import path, re_path
from . import views

urlpatterns = [
    path('net_stats/', views.StatsList.as_view()),
    # path('net_stats/<int:pk>/', views.StatsDetail.as_view()),

    path('file/details/<str:uuid>/', views.FileDetail.as_view()),
    path('files/', views.FilePathList.as_view()),
]
