from django.db import models
from django.urls import reverse

class Obyekt(models.Model):
	title = models.CharField(max_length=150)
	aftor  = models.TextField(blank=True)
	tavsif = models.TextField(blank = True)
	created_at = models.DateTimeField(auto_now_add=True)
	nashri = models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='photos/%Y/%m/%d')
	is_published = models.BooleanField(default=True)

	bolim = models.ForeignKey('Bolim',on_delete=models.PROTECT, null = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('view_libnews', kwargs={'libnews_id':self.pk})

	class Meta:
		verbose_name = "Kitob"
		verbose_name_plural = "Kitoblar"
	


	def myFunk(self):
		return "Beshikdan to qabrgacha ilm izla!!! wwww.mybook.uz"


class Bolim(models.Model):
	title = models.CharField(max_length=150,db_index=True,verbose_name='Kategoriya nomi')

	def get_absolute_url(self):
		return reverse('bolim', kwargs={'bolim_id':self.pk})


	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = "Kategoriya"
		verbose_name_plural ="Kategoriyalar"
		ordering = ['title']

