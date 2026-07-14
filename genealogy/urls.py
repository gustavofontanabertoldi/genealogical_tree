from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trees", views.trees, name="trees"),
    path("trees/<int:id>/", views.view_tree, name="view_tree"),
    path("trees/<int:id>/add_person", views.add_person, name="add_person"),
]
