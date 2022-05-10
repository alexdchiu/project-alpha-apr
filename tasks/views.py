from typing import List
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
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


class TaskListView(LoginRequiredMixin, ListView):
  model = Task
  template_name = "tasks/list.html"
  context_object_name = "taskslist"

  def get_queryset(self):
    return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ["is_completed"]
  success_url = reverse_lazy("somewhere")

  def get_success_url(self):
    return reverse('show_my_tasks')