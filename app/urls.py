
from django.urls import path
from app import views
urlpatterns = [
    # path('', views.index),
    path("", views.home, name="home"),
    path("form/", views.student_form, name="form"),
]