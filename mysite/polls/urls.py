from django.urls import pathspec

from . import views

urlpatterns = [
    path("", view.index, name="index"),
]