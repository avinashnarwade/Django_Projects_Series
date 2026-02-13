from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Todo 
from .serializers import TodoSerializer 

@api_view(['GET'])
def get_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data)