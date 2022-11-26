from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class GetAllTasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GetTasksByUserIDView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Task.objects.filter(user = user_id)
        return queryset

@api_view(['GET'])
def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status = 200)
    except:

        return Response({"msg": "No existe ninguna tarea con ese ID"}, status = 404)