from django.db import models 
from django.urls import reverse
import uuid
# Create your models here.
class Instrumento(models.Model):
    #Model representing a book genre."""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID INSTRUMENTO')
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=1000, help_text='Descripción del instrumento.')
	
	
	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('instrumento-detail', args=[str(self.id)])	