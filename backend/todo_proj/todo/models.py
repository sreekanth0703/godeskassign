from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TODO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, default='')
    description = models.TextField(default='')

    class Meta:
        db_table = 'TODO'

    def __unicode__(self):
        return self.title
