# Generated by Django 4.1.1 on 2022-10-04 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_remove_qualityplan_metricplan_qualityplan_metricplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='crops',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]