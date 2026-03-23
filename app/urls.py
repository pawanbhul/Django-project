
from django.urls import path
from app import views
urlpatterns = [
    # path('', views.index),
    path("", views.home, name="home"),
    path("form/", views.Student_form, name="form"),
    path("update/<int:id>/", views.update_student, name="update_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
]