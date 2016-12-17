from django.db import models
from datetime import datetime

# Create your models here.
class Datamain(models.Model):
	main_task = models.CharField(max_length=100)
	date_time = models.DateField()
	efforts = models.CharField(max_length=50)
	def __str__(self):
		return self.main_task + ' - ' + self.efforts


class Subtask(models.Model):
	sub_task = models.CharField(max_length=100)
	comments = models.CharField(max_length=50)

	def __str__(self):
		return self.sub_task + ' - ' + self.comments


	