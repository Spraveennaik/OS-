# Generated by Django 2.0.3 on 2018-04-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synchro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synchroalg',
            name='demourl',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
