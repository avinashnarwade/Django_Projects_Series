from django.urls import path
from app3.views import add_view,home

urlpatterns = [
    path('add_view/<int:n1>/<int:n2>/',add_view),
    path('home/',home),
]
