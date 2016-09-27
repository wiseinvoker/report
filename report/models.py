from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
	reporter = models.ForeignKey(User, related_name='posted_reports')
	task = models.TextField(blank=True)
	learning = models.TextField(blank=True)
	plan = models.TextField(blank=True)
	data = models.TextField(blank=True)
	outing = models.TextField(blank=True)
	other = models.TextField(blank=True)
	suggestion = models.TextField(blank=True)
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)

	class Meta:
		ordering = ('-id', )

