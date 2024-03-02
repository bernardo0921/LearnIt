from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'what is matter in the real world'},
    {'id': 1, 'name': 'Who is Jesus'},
    {'id': 1, 'name': 'I am in Ghana'},
]
# Create your views here.
def Home(request):
    contents = {"rooms": rooms}
    return render(request, "Home.html")

def Students(request):
    return render(request, "Student.html")