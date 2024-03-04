from django.shortcuts import render
from django.http import HttpResponse
rooms = [
    {'id': 1, 'name': 'what is matter in the real world'},
    {'id': 2, 'name': 'Who is Jesus'},
    {'id': 3, 'name': 'I am in Ghana'},
]
# Create your views here.
def Home(request):
    contents = {"rooms": rooms}
    return render(request, "./base/Home.html", contents)

def Students(request, pk):
    contents = {"rooms": rooms}
    return render(request, "./base/room.html", contents)

def indexes(request):
    return render(request, "./base/indexes.html")