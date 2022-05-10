from distutils.log import Log
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from projects.models import Project


# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
  model = Project
  template_name = "projects/list.html"
  context_object_name = "projectslist"

  def get_queryset(self):
    return Project.objects.filter(members=self.request.user)

class ProjectDetailView(LoginRequiredMixin, DetailView):
  model = Project
  template_name = "projects/detail.html"

class ProjectCreateView(LoginRequiredMixin, CreateView):
  model = Project
  template_name = "projects/create.html"
  fields = ["name", "description", "members"]
  success_url = reverse_lazy("somewhere")
  pk = None

  def form_valid (self, form):
    item = form.save()
    self.pk = item.pk
    return super(ProjectCreateView, self).form_valid(form)

  def get_success_url(self):
    return reverse('show_project', kwargs = {'pk':self.pk})