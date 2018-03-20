from django.db import models
from blocks.models import Sample

class spectrum(models.Model):
    spectrum_name = models.CharField(max_length=30)
    spectrum_type = models.CharField(max_length=30)
    Date_measured = models.DateField()
    Measure_condition = models.TextField(max_length=300)
    sample = models.ForeignKey(Sample,null=True,blank=True)
    def __str__(self):
        return self.spectrum_name
    class Meta:
        ordering = ['spectrum_name']



