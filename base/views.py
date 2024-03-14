from django.shortcuts import render
# from django.http import HttpResponse
from .models import Room
rooms = [
    {'id': 1, 'name': 'what is matter in the real world'},
    {'id': 2, 'name': 'Who is Jesus'},
    {'id': 3, 'name': 'I am in Ghana'},
]
# Create your views here.
def Students(request, pk):
    # roooms = Room.objects.get(id = pk)
    contents = {"rooms": rooms}
    return render(request, "./base/room.html", contents)

def indexes(request):
    return render(request, "./base/indexes.html")

# creating a view to work with the database
def Home(request):
    rooms = Room.objects.all()
    contenents = {"rooms": rooms}
    return render(request, "./base/Home.html", contenents)