from rest_framework import viewsets
from projects.models import Project, Task
from projects.serializers import (
    ProjectSerializer,  TaskSerializer
    )

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

