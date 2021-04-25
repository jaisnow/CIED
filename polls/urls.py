from django.urls import path

from . import views

urlpatterns = [
    path('score-list/', views.ScoreList.as_view()),
]