from django.db import models
  
# Create your models here.

class Sightings(models.Model):

    Latitude = models.FloatField()

    Longitude = models.FloatField()

    Unique_Squirrel_ID = models.CharField(max_length = 100)   
          
    SHIFT =(
            ('AM','AM'),
            ('PM','PM'),
            )
      
    Shift = models.CharField(
            choices=SHIFT, 
            max_length = 4, 
            )
    
    Date = models.DateField( 
            #max_length = 8,
            #help_text="Please use the following format: MMDDYYYY.",   
            )
    
    AGE =(
            ('Adult','Adult'),
            ('Juvenile','Juvenile'),
            ('?','?'),
            )

    Age = models.CharField(
            choices=AGE,
            max_length = 50,
            default = '',
            blank = True,
            )

    FUR_CHOICES=(
            ('Gray','Gray'),
            ('Cinnamon','CInnamon'),
            ('Black', 'Black')
            )

    Primary_Fur_Color = models.CharField(
            choices=FUR_CHOICES,
            max_length = 100,
            default = '',
            blank = True,
            )
    
    LOCATION = (
            ('Ground Plane','Ground Plane'),
            ('Above Ground','Above Ground'),
            )

    Location = models.CharField(
            choices = LOCATION,
            max_length = 100,
            default = '',
            blank = True,
            )

    Specific_Location = models.CharField(
            max_length = 100,
            default = '',
            blank = True,
            )

    Running = models.BooleanField()

    Chasing = models.BooleanField()

    Climbing = models.BooleanField()

    Eating = models.BooleanField()
    
    Foraging = models.BooleanField()

    Other_Activities = models.CharField(
            max_length = 500,
            default = '',
            blank = True,
            )

    Kuks = models.BooleanField()

    Quaas = models.BooleanField()

    Moans = models.BooleanField()

    Tail_flags = models.BooleanField()

    Tail_twitches = models.BooleanField()

    Approaches = models.BooleanField()

    Indifferent = models.BooleanField()

    Runs_from = models.BooleanField()
