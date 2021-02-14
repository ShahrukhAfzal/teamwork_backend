from rest_framework import serializers
from projects.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'tasks')
        read_only_fields = ('id', 'tasks')


class ProjectReadSerializer(ProjectSerializer):
    tasks = TaskSerializer(many=True)
