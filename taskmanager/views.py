from rest_framework import viewsets
from taskmanager.models import TemporaryUser, Task
from taskmanager.serializers import TaskSerializer

class TaskView(viewsets.ModelViewSet):
    action_serializers = {
        'list': TaskSerializer
    }

    def get_serializer_class(self):
        return self.action_serializers.get(
            self.action,
            self.serializer_class
        )

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(temp_user=user_id)
