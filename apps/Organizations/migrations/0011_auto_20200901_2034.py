# Generated by Django 3.0.7 on 2020-09-02 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0010_organization_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='monday_from',
            field=models.TimeField(blank=True, default='20:00'),
        ),
    ]
