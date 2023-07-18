from django.urls import path
from SSR import views

urlpatterns = [
    path("", views.home, name="home"),
]