from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    #============
    # Tree (urls)
    #============

    path("trees/", views.trees, name="trees"),
    
    path("trees/create/", views.create_tree, name="create_tree"),

    path(
        "trees/<int:tree_id>/",
        views.view_tree,
        name="view_tree",
    ),
    
    #============
    # Person (urls)
    #============

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
    
    #============
    # Event (urls)
    #============
    
    path(
        "trees/<int:tree_id>/event/create_event_for_tree/",
        views.create_event_for_tree,
        name="create_event_for_tree"
    ),
    
    path(
        "trees/<int:tree_id>/persons/<int:person_id>/event/create_event_for_person",
        views.create_event_for_person,
        name="create_event_for_person"
    ),
    
    path(
        "trees/<int:tree_id>/event/view_event/<int:event_id>/",
        views.view_event,
        name="view_event"
    ),
    
    path(
        "trees/<int:tree_id>/event/view_event/<int:event_id>/add_participant/",
        views.add_participant,
        name="add_participant"
    ),
]
