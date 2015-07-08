from django.db import models
from django.template.defaultfilters import slugify

class Ingridient(models.Model):
	title = models.TextField(max_length=500)
	slug = models.SlugField(blank=True)
	description = models.TextField(max_length=500,blank=True,null=True)
	
	def __unicode__(self):
		return self.title

class Portion(models.Model):
	ingridient = models.ForeignKey(Ingridient)
	ammount = models.TextField(max_length=200,blank=True,null=True)
	description = models.TextField(max_length=500,blank=True,null=True)
	
	def __unicode__(self):
		return self.ammount

class Step(models.Model):
	instructions = models.TextField(max_length=2000)
	note = models.TextField(max_length=500,blank=True,null=True)

	def __unicode__(self):
		return self.instructions	

class Food(models.Model):
	title = models.TextField(max_length=500)
	slug = models.SlugField(blank=True)
	ingridients = models.ManyToManyField(Portion, blank=True,null=True)
	steps = models.ManyToManyField(Step, blank=True,null=True)
	time_in_minutes = models.IntegerField(blank=True,null=True)
	link = models.URLField(blank=True,null=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Food, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title