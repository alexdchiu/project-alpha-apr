from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField("auth.User", related_name="projects")

    def __str__(self):
        return self.name
