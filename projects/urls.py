from django.urls import path
from projects.models import Project

from projects.views import (
  ProjectListView,
  ProjectDetailView,
)

urlpatterns = [
  path("", ProjectListView.as_view(),name="list_projects"),
  path("<int:pk>/", ProjectDetailView.as_view(),name="show_project"),
]