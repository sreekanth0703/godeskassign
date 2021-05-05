from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64, default='')
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Project'

class TODO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default='')
    description = models.TextField(default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='todoProject')
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'TODO'

    def __unicode__(self):
        return self.title


class UserProjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, related_name='userProject')

    class Meta:
        db_table = 'USER_PROJECTS'
