# Generated by Django 3.0.7 on 2020-09-02 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0008_auto_20200901_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_from', models.TimeField(blank=True)),
                ('monday_to', models.TimeField(blank=True)),
                ('tueday_from', models.TimeField(blank=True)),
                ('tueday_to', models.TimeField(blank=True)),
                ('wednesday_from', models.TimeField(blank=True)),
                ('wednesday_to', models.TimeField(blank=True)),
                ('thursday_from', models.TimeField(blank=True)),
                ('thursday_to', models.TimeField(blank=True)),
                ('friday_from', models.TimeField(blank=True)),
                ('friday_to', models.TimeField(blank=True)),
                ('saturday_from', models.TimeField(blank=True)),
                ('saturday_to', models.TimeField(blank=True)),
                ('sunday_from', models.TimeField(blank=True)),
                ('sunday_to', models.TimeField(blank=True)),
                ('isActive', models.BooleanField(default=True)),
                ('createdBy', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastUpdatedBy', models.CharField(blank=True, max_length=200)),
                ('lastUpdated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
