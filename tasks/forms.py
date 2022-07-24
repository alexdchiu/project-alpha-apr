from django.forms import ModelForm
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.models import User

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ["name", "start_date", "due_date", "project","assignee"]
  
  def __init__(self, *args, **kwargs):
    user = kwargs.pop("user")
    super(TaskForm, self).__init__(*args, **kwargs)
    self.fields["project"].queryset = Project.objects.filter(members=user)
    # self.fields["assignee"].queryset = Task.objects.filter(assignee=user)
    print(Task)


