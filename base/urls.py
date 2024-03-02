from django.urls import path
from .views import Home, Students

# create url patterns for the base app
urlpatterns = [
    path('', Home, name = 'home'),
    path('student/', Students, name = "student"),
]
