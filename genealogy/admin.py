from django.contrib import admin
from .models import Document, Event, EventParticipant, Person, Tree

admin.site.register(Tree)
admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Event)
admin.site.register(EventParticipant)
