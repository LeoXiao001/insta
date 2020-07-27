from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HelloDjango.as_view()),
]
