from django.urls import path
from .views import Home, Students, indexes

# create url patterns for the base app
urlpatterns = [
    path('', Home, name = 'home'),
    path('student/', Students, name = "student"),
    path('indexes/', indexes, name = "indexes")
]
