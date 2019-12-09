# GROUP30: Squirrel Tracker

## Description
### What is it?
We aim at  keeping track of all the known squirrels and plans to start with Central Park for our client. Therefore, we built an application that can import the [2018 Central Park Squirrel Census data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) and allow his team to add, update, and view squirrel data. 

### Main Features
**Management commands:**
* Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
`$ python manage.py import_squirrel_data /path/to/file.csv`
* Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
`$ python manage.py export_squirrel_data /path/to/file.csv`

**Views**
* `/map` A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map
* `/sightings` A view that lists all squirrel sightings with links to edit each
* `/sightings/<unique-squirrel-id>` A view to update a particular sighting
* `/sightings/add` A view to create a new sighting
* `/sightings/stats` A view with general stats about the sightings


## Group and section
Project Group 30, Section 1

## Group Members
Yuming Huang, Zitong Peng

UNIs: [yh3190, zp2215]

## The link to the server running our application
