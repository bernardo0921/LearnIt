from django.shortcuts import render
from django.http import HttpResponse
rooms = [
    {'id': 1, 'name': 'what is matter in the real world'},
    {'id': 1, 'name': 'Who is Jesus'},
    {'id': 1, 'name': 'I am in Ghana'},
]
# Create your views here.
def Home(request):
    contents = {"rooms": rooms}
    return render(request, "./base/Home.html", contents)

def Students(request):
    return render(request, "./base/Student.html")

def indexes(request):
    return render(request, "./base/indexes.html")