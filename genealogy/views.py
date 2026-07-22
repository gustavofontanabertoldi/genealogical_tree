from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Document, Event, EventParticipant, Person, Tree
from.forms import PersonForm, TreeForm, EventForm, EventParticipantForEventForm, EventParticipantForPersonForm

#============
# Index (views)
#============

def index(request):
    return render(request, "genealogy/home.html")

#============
# Tree (views)
#============

def trees(request):
    tree_list = Tree.objects.all()
    context = {"trees":tree_list}
    return render(request, "genealogy/tree/trees.html", context)

def view_tree(request, tree_id):
    tree = get_object_or_404(Tree, pk=tree_id)
    context = {
        "tree": tree,
        "persons": tree.persons.all()
    }
    return render(request, "genealogy/tree/view_tree.html", context)

def create_tree(request):
    if request.method == "POST":
        form = TreeForm(request.POST)
        if form.is_valid():
            tree = form.save()
            return redirect("view_tree", tree_id=tree.id)
    else:
        form = TreeForm()
        context = {
            "form": form
        }
        return render(request, "genealogy/tree/create_tree.html", context)

#============
# Person (views)
#============

def add_person(request, tree_id):
    tree = get_object_or_404(Tree, pk=tree_id)
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.tree = tree
            person.save()
            return redirect("view_tree", tree_id=tree.id)
    else:
        form = PersonForm()
    
    context = {
            "form":form,
            "tree":tree 
        }
    return render(request, "genealogy/person/add_person.html", context)

def view_person(request, tree_id, person_id):
    person = get_object_or_404(Person, pk=person_id)
    participations = EventParticipant.objects.filter(person=person)
    context = {
        "person": person,
        "participations": participations,
    }
    return render(request, "genealogy/person/view_person.html", context)

#============
# Event (views)
#============

def create_event_for_tree(request, tree_id):
    tree = get_object_or_404(Tree, pk=tree_id)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.tree = tree
            event.save()
            return redirect("view_event", tree_id=tree_id, event_id=event.id)
    else:
        form = EventForm()
    context = {
        "form":form,
        "tree":tree
    }
    return render(request, "genealogy/events/create_events_for_tree.html", context)

def create_event_for_person(request, tree_id ,person_id):
    person = get_object_or_404(Person, pk=person_id)
    tree = get_object_or_404(Tree, pk=tree_id)
    if request.method == "POST":
        form = EventForm(request.POST)
        role_form = EventParticipantForPersonForm(request.POST)
        if form.is_valid() and role_form.is_valid():
            event = form.save(commit=False)
            event.tree = tree
            event.save()
            participation = role_form.save(commit=False)
            participation.person = person
            participation.event = event
            participation.save()
            return redirect("view_event", tree_id=tree_id, event_id=event.id)
    else:
        form = EventForm()
        role_form = EventParticipantForPersonForm()
    context = {
        "form":form,
        "role_form":role_form,
        "person":person
    }
    return render(request, "genealogy/events/create_event_for_person.html", context)

def add_participant(request, tree_id, event_id):
    event = get_object_or_404(Event, pk=event_id, tree_id=tree_id)
    tree = get_object_or_404(Tree, pk=tree_id)
    if request.method == "POST":
        form = EventParticipantForEventForm(request.POST)
        form.fields["person"].queryset = tree.persons.all()
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = event
            participant.save()
            return redirect("view_event", tree_id=tree_id, event_id=event.id)
    else:
        form = EventParticipantForEventForm()
        form.fields["person"].queryset = tree.persons.all()
        context = {
            "form":form,
            "event":event
        }
        return render(request, "genealogy/events/add_participant.html", context)

def view_event(request, tree_id, event_id):
    event = get_object_or_404(Event, pk=event_id, tree_id=tree_id)
    participations = EventParticipant.objects.filter(event=event).select_related("person")
    context = {
        "event":event,
        "participations":participations,
    }
    return render(request, "genealogy/events/view_event.html", context)