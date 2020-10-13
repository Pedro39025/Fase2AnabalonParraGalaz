from django.db import models

# Create your models here.
class Instrumento(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name