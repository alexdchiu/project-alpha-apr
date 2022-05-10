from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from tasks.models import Task

# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
  model = Task
  template_name = "tasks/create.html"
  fields = ["name", "start_date", "due_date", "project", "assignee"]
  success_url = reverse_lazy("somewhere")
  pk = None

  def form_valid (self, form):
    item = form.save()
    self.pk = item.project.pk
    return super(TaskCreateView, self).form_valid(form)

  def get_success_url(self):
    return reverse('show_project', kwargs = {'pk':self.pk})

