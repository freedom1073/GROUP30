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

    Running = BooleanField()
    Chasing = BooleanField()
    Climbing = BooleanField()
    Eating = BooleanField()
    Foraging = BooleanField()
    Other_Activities = models.CharField()
    Kuks = BooleanField()
    Quaas = BooleanField()
    Moans = BooleanField()
    Tail_flags = BooleanField()
    Tail_twitches = BooleanField()
    Approaches = BooleanField()
    Indifferent = BooleanField()
    Runs_from = BooleanField()

