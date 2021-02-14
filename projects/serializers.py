from rest_framework import serializers
from projects.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
