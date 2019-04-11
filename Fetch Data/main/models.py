from django.db import models

# Create your models here.


class PlayerData(models.Model):
	NAME = models.TextField()
	STATUS = models.TextField()
	
	def __str__(self):
		return self.NAME