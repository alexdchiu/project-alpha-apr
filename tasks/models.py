from django.db import models
from django.db.models import Count, Case, When

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project", related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        "auth.User", null=True, related_name="tasks", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
    
    def get_form_kwargs(self):
        kwargs = super(Task)
    
    def get_queryset(self):
        Task.aggregate(bool_col=Count(Case(When(is_completed=True, then=1))))
