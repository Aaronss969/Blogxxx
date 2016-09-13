from django.db import models
from django.utils import timezone
# Create your models here.
class Entrada(models.Model):
	
	ESTATUS_CHOICES= (
		('borrador','Borrador'),
		('actualizado','Actualizado')
		)

	titulo= models.CharField(max_length=140)

	creado= models.DateTimeField(auto_now_add=True)

	cuerpo= models.TextField()

	slug= models.SlugField(max_length=249, unique_for_date='publicado')

	publicado= models.DateTimeField(default=timezone.now)

	actualizado= models.DateTimeField(auto_now=True)

	estatus= models.CharField(max_length=10, choices= ESTATUS_CHOICES, default='borrador')

	def __str__(self):
		return self.titulo


