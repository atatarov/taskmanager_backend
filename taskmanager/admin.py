from django.contrib import admin

from .models import Task, TemporaryUser

admin.site.register(Task)
admin.site.register(TemporaryUser)
