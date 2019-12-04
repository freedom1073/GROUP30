from django.core.management.base import BaseCommand, CommandError
from census.models import Sightings
import csv

class Command(BaseCommand):
    help = 'Import squirrel data from existing csv file.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Please enter the path to the csv file.')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                b = Sightings(
                        Latitude = row['Y'],
                        Longitude = row['X'],
                        Unique_Squirrel_ID = row['Unique Squirrel ID'],  
                        Shift = row['PM'],
                        Date = row['Date'],
                        Age = row['Age'],
                        Primary_Fur_Color = row['Primary Fur Color'],
                        Location = row['Location'],
                        Specific_Location = row['Specific Location'],
                        Running = row['Running'],
                        Chasing = row['Chasing'],
                        Climbing = row['Climbing'],
                        Eating = row['Eating'],
                        Foraging = row['Foraging'],
                        Other Activities = row['Other Activities'],
                        Kuks = row['Kuks'],
                        Quaas = row['Quaas'],
                        Moans = row['Moans'],
                        Tail_flags = row['Tail flags'],
                        Tail_twitches = row['Tail twitches'],
                        Approaches = row['Approaches'],
                        Indifferent = row['Indifferent'],
                        Runs_from = row['Runs from'],
                        )
                b.save()

            self.stdout.write(self.style.SUCCESS('Congratulations! Successfully import data.'))
