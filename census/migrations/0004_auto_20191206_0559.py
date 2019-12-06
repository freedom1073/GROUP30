# Generated by Django 3.0 on 2019-12-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0003_auto_20191206_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Date',
            field=models.CharField(blank=True, help_text='Please use the following format: MMDDYYYY.', max_length=8),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Longitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Other_Activities',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'CInnamon'), ('Black', 'Black')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Shift',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=4),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Specific_Location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Unique_Squirrel_ID',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
