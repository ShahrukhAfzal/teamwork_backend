from rest_framework import serializers
from projects.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'project_name', 'project',
                'start_date', 'end_date', 'created_at', 'modified_at')

    def get_project_name(self, obj):
        return obj.project.name


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'tasks',
            'start_date', 'end_date', 'avatar')
        read_only_fields = ('id', 'tasks')

