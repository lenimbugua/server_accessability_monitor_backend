from django.urls import path, re_path
from . import views

urlpatterns = [
    path('ping/', views.Ping.as_view()),

    path('file/details/<str:uuid>/', views.FileDetail.as_view()),
    path('files/', views.FilePathList.as_view()),
]
