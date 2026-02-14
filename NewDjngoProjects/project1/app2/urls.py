from django.urls import path
from app2.views import add,sub


urlpatterns = [
    path('add/',add),
    path('sub/',sub),
]
