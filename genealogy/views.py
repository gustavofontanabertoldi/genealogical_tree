from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Document, Event, EventParticipant, Person, Tree
from.forms import PersonForm, TreeForm

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

def view_tree(request, id):
    tree = get_object_or_404(Tree, pk=id)
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
            return redirect("view_tree", id=tree.id)
    else:
        form = TreeForm()
        context = {
            "form": form
        }
        return render(request, "genealogy/tree/create_tree.html", context)

#============
# Person (views)
#============

def add_person(request, id):
    tree = get_object_or_404(Tree, pk=id)
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.tree = tree
            person.save()
            return redirect("view_tree", id=tree.id)
    else:
        form = PersonForm()
    
    context = {
            "form":form,
            "tree":tree 
        }
    return render(request, "genealogy/person/add_person.html", context)