from pydoc import plain
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MetricPlan(models.Model):
    name = models.CharField('name', max_length=100)
    desc = models.TextField(blank=True)
    type = models.CharField('Type', max_length=50)
    value = models.IntegerField()
    start_day = models.DateTimeField('startday')
    end_day = models.DateTimeField('EndDay')

    def __str__(self):
        return self.name
    

class QualityPlan(models.Model):
    name = models.CharField('name', max_length=100)
    desc = models.TextField(blank=True)
    metricplan = models.ManyToManyField(
    MetricPlan, blank=True, null=True)

    def __str__(self):
        return self.name


class Crops(models.Model):
    name=models.CharField('Name',max_length=100)
    desc = models.TextField(blank=True)
    type=models.CharField('Type',max_length=50)
    user=models.IntegerField("Created By",blank=False,default=1)
    def __str__(self):
        return self.name

class GrowPlan(models.Model):
    name = models.CharField('Name', max_length=100)
    desc = models.TextField(blank=True)
    date = models.DateTimeField('Day')
    qualityplan = models.ForeignKey(
        QualityPlan, blank=True, null=True, on_delete=models.CASCADE)
    crop = models.ForeignKey(
        Crops, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





