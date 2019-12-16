from django.db import models

class forum(models.Model):
	email = models.EmailField(max_length=70, null=False, blank=False, unique=False)
	title = models.CharField(max_length=100)
	post_text = models.TextField()
	def __str__(self):
		return self.title