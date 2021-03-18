from django.db import models
from django.urls import reverse

class Blog_post(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=20)
	body = models.TextField(max_length=300)

	def __str__(self):
		return self.title

#	def get_absolute_url(self):
#		return reverse('post_detail',args=(str(self.id)))