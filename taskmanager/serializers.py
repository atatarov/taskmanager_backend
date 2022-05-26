from rest_framework import serializers
from taskmanager.models import TemporaryUser, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','temp_user', 'description', 'deadline', 'color', 'repeating_days', 'is_archive', 'is_favorite')


class TemporaryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryUser
        fields = ('id')
