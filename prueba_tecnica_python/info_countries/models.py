from django.db import models

# Create your models here.

class Country(models.Model):
	"""
    Clase usada para gestionar la informacion de un pais
    - - - - -
    Attributes
    - - - - -
    region : string[30]
		Region a la cual pertenece el pais
	name : string[30]
        Nombre del pais
	time : string[30]
		Tiempo tardado en armar la fila
    """
	region = models.CharField(
		max_length=30, 
		blank=False,
		null=False
		)
	name = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		unique=True
		)
	time = models.CharField(
		max_length=70, 
		blank=False,
		null=False
		)
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
	def __str__(self):
		return self.name
	
	
class LanguageCountry(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	_language = models.CharField(
		max_length=50, 
		blank=False,
		null=False
		)
	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'
	def __str__(self):
		return self.language
	def get_language(self):
		return self._language
	def set_language(self, language):
		self._language = language