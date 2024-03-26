from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    creation_date = models.DateTimeField('creation date')
    end_date = models.DateTimeField('end date', null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def length(self):
        if self.end_date:
            time_delta = self.end_date - self.creation_date
            days = time_delta.days
            hours = time_delta.seconds // 3600
            minutes = (time_delta.seconds % 3600) // 60
            return f"{days} jours, {hours} heures, {minutes} minutes"
        else:
            return f"Le projet n'est pas terminé"
    

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    creation_date = models.DateTimeField('creation date')
    end_date = models.DateTimeField('end date')
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Users(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    