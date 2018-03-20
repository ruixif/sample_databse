from django.db import models
from functions.models import *


# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=30)
    Sample_type = models.ForeignKey(sample_type)
    date_created = models.DateField()
    date_removed_optional = models.CharField(blank=True,max_length=30)
    Class = models.ForeignKey(Sample_Class)
    location = models.ForeignKey(dewar_tray)
    provider_name = models.ForeignKey(Author)
    sample_description_optional = models.TextField(max_length=500,blank=True)
    change_log_optional = models.TextField(max_length=500,blank=True)
    #spectrum_optional = models.ManyToManyField(spectrum_data,blank=True,limit_choices_to)
    #spectrum_optional = models.ManyToManyField(spectrum_data,blank=True)
    publication_optional = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']



