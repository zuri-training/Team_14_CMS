from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Website(models.Model):
	"""
		Model class for building the website
		args:
			title: Name of the website
			html: Html Part of the website
			css: Css part of the website
			author: Owner of the website
	"""
	title = models.CharField(max_length=300)
	html = models.TextField()
	css = models.TextField()
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		""" Method for describing the website """
		return self.title
