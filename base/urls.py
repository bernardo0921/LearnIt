from django.urls import path
from .views import Home, Students, indexes, createRoom

# create url patterns for the base app
urlpatterns = [
    path('', Home, name = "home"),
    path('ss/', indexes, name = "indexes"),
    path('student/<str:pk>', Students, name = "student"),
    path('roomform/', createRoom, name = "createroom"),
]
