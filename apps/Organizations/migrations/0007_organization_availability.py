# Generated by Django 3.0.7 on 2020-09-01 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0006_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='availability',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Organizations.Availability'),
        ),
    ]