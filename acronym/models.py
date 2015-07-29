from datetime import *

from django.db import models
from django.utils import timezone


# Create your models here.
class AcronymManager(models.Manager):
    def create_acronym(self, short_text, long_text, pub_date=None, realm=None, 
            description=None, ref=None):

        acronym = self.create(short_text=short_text, long_text=long_text, 
                pub_date=pub_date, realm=realm, description=description, 
                ref=ref)
        # do something with the acro
        return acronym


class Acronym(models.Model):
    short_text = models.CharField(max_length=10)
    long_text = models.CharField(max_length=200)
    pub_date = models.DateField('date created', blank=True)
    realm = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    ref = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return self.short_text
    
    def was_published_recently(self):
        return self.pub_date >= date.today().replace(day=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    objects = AcronymManager()
    
