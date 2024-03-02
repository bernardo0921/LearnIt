from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, "Home.html")

def Students(request):
    return render(request, "Student.html")