# Generated by Django 4.1.1 on 2022-09-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
