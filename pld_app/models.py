from django.db import models
import datetime
from django.utils import timezone

class Plant(models.Model):

	plant_leaf_image = models.ImageField(blank=True, null = True, upload_to = "images/%Y/%m/%d")
	name = models.CharField(max_length=150 , null=True, blank=True)

	def __str__(self):
		if self.name:
			if self.name != 'None':
				if self.name != None:
					return self.name
				else:
					return ''
			else:
				return ''
		else:
			return ''




class Prediction(models.Model):

	predictions = models.CharField(max_length=150 , null=True, blank=True)
	prediction_image = models.ImageField(blank=True, null = True, upload_to = "images/%Y/%m/%d")

	def __str__(self):
		if self.predictions:
			if self.predictions != 'None':
				if self.predictions != None:
					return self.predictions
				else:
					return ''
			else:
				return ''
		else:
			return ''




class Contact(models.Model):

	name = models.CharField(max_length=150 , null=True, blank=True)
	number = models.CharField(max_length=150 , null=True, blank=True)
	email = models.CharField(max_length=150 , null=True, blank=True)
	message = models.CharField(max_length=150 , null=True, blank=True)

	def __str__(self):
		if self.name:
			if self.name != 'None':
				if self.name != None:
					return self.name
				else:
					return ''
			else:
				return ''
		else:
			return ''
