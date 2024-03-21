from django.shortcuts import render
from .models import Room
from .forms import RoomForm
rooms = [
    {'id': 1, 'name': 'what is matter in the real world'},
    {'id': 2, 'name': 'Who is Jesus'},
    {'id': 3, 'name': 'I am in Ghana'},
]
# Create your views here.
def Students(request, pk):
    # roooms = Room.objects.get(id = pk)
    contents = {"rooms": Room}
    return render(request, "./base/room.html", contents)

def indexes(request):
    return render(request, "./base/indexes.html")

# creating a view to work with the database
def Home(request):
    rooms = Room.objects.all()
    contenents = {"rooms": rooms}
    return render(request, "./base/Home.html", contenents)
def createRoom(request):
    form = RoomForm
    contents = {"form": form}
    return render(request, "./base/room_form.html", contents)