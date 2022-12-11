from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogpage"),
    path("blogpost/<int:id>", views.blogpost, name="blogpage")
]