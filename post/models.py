from django.db import models

# Create your models here.
class Post(models.Model):

	id_blog =  models.AutoField(primary_key=True)
	author = models.CharField(max_length=140)
	title = models.CharField(max_length=140)

	def __str__(self):
		return self.title