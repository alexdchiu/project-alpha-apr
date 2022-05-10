from django.contrib import admin


from projects.models import Project
from tasks.models import Task


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
