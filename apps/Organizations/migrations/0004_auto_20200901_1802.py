# Generated by Django 3.0.7 on 2020-09-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0003_remove_availability_updatedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='lastUpdated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='lastUpdatedBy',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]