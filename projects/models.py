from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # avatar= models.ImageField(upload_to='')

    def __str__(self):
        return f"Project {self.id}. {self.name}"


class Task(models.Model):
    name =  models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project,
            on_delete=models.CASCADE,
            related_name='tasks'
        )

    def __str__(self):
        return f"Task -> {self.name}"
