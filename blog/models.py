from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
	      default=timezone.now)
	published_date = models.DateTimeField(
	      blank=True, null=True)
	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	YEAR_IN_SCHOOL_CHOICES = (
	  (FRESHMAN, 'Freshman'),
	  (SOPHOMORE, 'Sophomore'),
	  (JUNIOR, 'Junior'),
	  (SENIOR, 'Senior'),
	)
	year_in_school = models.CharField(
	  max_length=2,
	  choices=YEAR_IN_SCHOOL_CHOICES,
	  default=FRESHMAN,
	)

	def publish(self):
	  self.published_date = timezone.now()
	  self.save()

	def __str__(self):
	  return self.title