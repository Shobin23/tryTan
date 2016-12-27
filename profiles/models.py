from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from simple_history.models import HistoricalRecords


# Create your models here.
class Datamain(models.Model):
    main_task = models.CharField(max_length=100)
    date_time = models.DateField()
    efforts = models.CharField(max_length=50)
    status=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('profiles:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.main_task + ' - ' + self.efforts


class Subtask(models.Model):
    sub_task = models.CharField(max_length=100)
    main_task = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
       return self.sub_task + ' - ' + self.comments

    def get_absolute_url(self):
        return reverse('profiles:detail')