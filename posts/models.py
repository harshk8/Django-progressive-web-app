from django.db import models

# Create your models here.
class feed(models.Model):
	id=models.IntegerField(primary_key=True)
	author=models.CharField(max_length=50)
	title=models.CharField(max_length=100)
	body=models.TextField()


	
class Traffic(models.Model):
	ip=models.GenericIPAddressField()
	created_at = models.DateTimeField(auto_now=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	timezone = models.CharField(max_length=255, null=True, blank=True)
	region = models.CharField(max_length=255, null=True, blank=True)
