# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Users(models.Model):

    #__Users_FIELDS__
    users = models.TextField(max_length=255, null=True, blank=True)
    username = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    namemain = models.TextField(max_length=255, null=True, blank=True)
    admin = models.BooleanField()

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class News(models.Model):

    #__News_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    detail = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__News_FIELDS__END

    class Meta:
        verbose_name        = _("News")
        verbose_name_plural = _("News")



#__MODELS__END
