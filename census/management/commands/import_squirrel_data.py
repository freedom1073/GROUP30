from django.core.management.base import BaseCommand, CommandError
from census.models import Sightings
import csv

class Command(BaseCommand):
    help = 'Import squirrel data from existing csv file.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Please enter the path to the csv file.')

    def handle(self, *args, **kwargs):
        def str_to_bool(s):
            if s=='true':
                return True
            if s=='false':
                return False

        with open(kwargs['path']) as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        for row in data:
            b = Sightings(
                    Latitude = float(row['Y']),
                    Longitude = float(row['X']),
                    Unique_Squirrel_ID = row['Unique Squirrel ID'],
                    Shift = row['Shift'],
                    Date = row['Date'][4:]+'-'+row['Date'][0:2]+'-'+row['Date'][2:4],
                    Age = row['Age'],
                    Primary_Fur_Color = row['Primary Fur Color'],
                    Location = row['Location'],
                    Specific_Location = row['Specific Location'],
                    Running = str_to_bool(row['Running']),
                    Chasing = str_to_bool(row['Chasing']),
                    Climbing = str_to_bool(row['Climbing']),
                    Eating = str_to_bool(row['Eating']),
                    Foraging = str_to_bool(row['Foraging']),
                    Other_Activities = row['Other Activities'],
                    Kuks = str_to_bool(row['Kuks']),
                    Quaas = str_to_bool(row['Quaas']),
                    Moans = str_to_bool(row['Moans']),
                    Tail_flags = str_to_bool(row['Tail flags']),
                    Tail_twitches = str_to_bool(row['Tail twitches']),
                    Approaches = str_to_bool(row['Approaches']),
                    Indifferent = str_to_bool(row['Indifferent']),
                    Runs_from = str_to_bool(row['Runs from']),
                    )
            b.save()
