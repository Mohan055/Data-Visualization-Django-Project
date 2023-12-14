from django.db import models

# Create your models here.

class DataModel(models.Model):
    end_year = models.BigIntegerField(null=True, blank=True, default=None)
    intensity = models.BigIntegerField(null=True, blank=True, default=None)
    sector = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    insight = models.CharField(max_length=500)
    url = models.URLField(max_length=500)
    region = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.BigIntegerField(null=True, blank=True, default=None)
    impact = models.BigIntegerField(null=True, blank=True, default=None)
    added = models.CharField(max_length=200, null=True, blank=True,default="")
    published = models.CharField(max_length=200,null=True, blank=True, default="")
    country = models.CharField(max_length=100, null=True, blank=True)
    relevance = models.BigIntegerField(null=True, blank=True, default=None)
    pestle = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    likelihood = models.BigIntegerField(null=True, blank=True, default=None)
    City = models.CharField(max_length=200,null=True, blank=True,default="")
    

    def __str__(self):
        return self.title