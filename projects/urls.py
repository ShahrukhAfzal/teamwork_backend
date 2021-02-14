from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
