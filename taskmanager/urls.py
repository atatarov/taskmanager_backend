from django.urls import path
from taskmanager.views import TaskView

pattern_user_id = '^(?P<user_id>.+)/'

urlpatterns = [
    path('tasks/', TaskView.as_view({
        'get': 'list',
    })),
    path('tasks/<int:user_id>/', TaskView.as_view({
        'get': 'list',
    }))
]
