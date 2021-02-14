from rest_framework import viewsets
from projects.models import Project, Task
from projects.serializers import (
    ProjectSerializer, ProjectReadSerializer, TaskSerializer
    )

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectReadSerializer

        if self.request.method == 'POST':
            return ProjectSerializer

            
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

