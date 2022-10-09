# Generated by Django 4.1.1 on 2022-10-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualityplan',
            name='metricplan',
        ),
        migrations.AddField(
            model_name='qualityplan',
            name='metricplan',
            field=models.ManyToManyField(blank=True, null=True, to='api.metricplan'),
        ),
    ]
