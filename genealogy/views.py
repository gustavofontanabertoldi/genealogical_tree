from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Document, Event, EventParticipant, Person, Tree

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
    context = {"tree": tree}
    return render(request, "genealogy/tree/view_tree.html", context)