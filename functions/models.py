from django.db import models
#predefined functions

class Author(models.Model):
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    email_optional = models.EmailField(blank=True)
    def __str__(self):
        return u'%s %s' %(self.first_name, self.last_name)


class Sample_Class(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class dewar_tray(models.Model):
    dewar_aphabet = models.CharField(max_length=30)
    tray_number_optional = models.CharField(max_length=5, blank=True)
    def __str__(self):
        return u'%s %s' %(self.dewar_aphabet, self.tray_number_optional)
    class Meta:
        ordering = ['dewar_aphabet']

class sample_type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class spectrum_data(models.Model):
    spectrum_name = models.CharField(max_length=30)
    spectrum_type = models.CharField(max_length=30)
    Date_measured = models.DateField()
    Measure_condition = models.CharField(max_length=30)
    def __str__(self):
        return self.spectrum_name
    class Meta:
        ordering = ['spectrum_name']

        
