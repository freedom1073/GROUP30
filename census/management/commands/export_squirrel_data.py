from django.core.management.base import BaseCommand, CommandError
from census.models import Sightings
import csv

class Command(BaseCommand):
    help = 'Export squirrels data to csv.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Please enter the path to save the csv file.')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path,'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Latitude', 'Longitude', 'Unique Squirrel ID', 'Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
            sightings = Sightings.objects.all().values_list('Latitude', 'Longitude', 'Unique_Squirrel_ID', 'Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from')
            for sighting in sightings:
                writer.writerow(sighting)


