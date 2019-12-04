from django.db import models

# Create your models here.

class Sightings(models.Model):
    
    Latitude = models.FloatField()
    
    Longitude = models.FloatField()

    Unique_Squirrel_ID = models.CharField()

    SHIFT =(
            ('AM','AM'),
            ('PM','PM'),
            )
    
    Shift = models.CharField(choices=SHIFT)

    Date = models.DateField()

    AGE =(
            ('Adult','Adult'),
            ('Juvenile','Juvenile'),
            )

    Age = models.CharField(choices=AGE)

    FUR_CHOICES=(
            ('Gray','Gray'),
            ('Cinnamon','CInnamon'),
            ('Black', 'Black'),
            )

    Primary_Fur_Color = models.CharField(choices=FUR_CHOICES)
    
    LOCATION = (
            ('Ground Plane','Ground Plane'),
            ('Above Ground','Above Ground'),
            )

    Location = models.CharField(choices = LOCATION)
     
    Specific_Location = models.CharField()

    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_Activities = models.CharField()
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()

