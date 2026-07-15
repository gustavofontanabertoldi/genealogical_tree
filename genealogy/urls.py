from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("trees/", views.trees, name="trees"),
    path("trees/create/", views.create_tree, name="create_tree"),

    path(
        "trees/<int:tree_id>/",
        views.view_tree,
        name="view_tree",
    ),

    path(
        "trees/<int:tree_id>/add_person/",
        views.add_person,
        name="add_person",
    ),

    path(
        "trees/<int:tree_id>/persons/<int:person_id>/",
        views.view_person,
        name="view_person",
    ),
]
