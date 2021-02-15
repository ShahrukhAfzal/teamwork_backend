from rest_framework import serializers
from projects.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'project')


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'tasks',
            'start_date', 'end_date', 'avatar')
        read_only_fields = ('id', 'tasks')

