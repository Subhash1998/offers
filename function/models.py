from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User,blank=False)
	company=models.CharField(max_length=200)

	def __unicode__(self):
		return self.user.username

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
	    if created:
	        UserProfile.objects.create(user=instance)


class Feature(models.Model):
	feature=models.ForeignKey(UserProfile)
	company_name=models.CharField(max_length=200)
	feature_name=models.CharField(max_length=200)
	feature_detail=models.TextField(max_length=10000)

	def __unicode__(self):
		return self.feature_name
