# E4501 Final Project: Squirrel Tracker

## Introduction
This is the final project of the course E4501 Tools for Analytics. In order to keep track of the squirrels in the Central Park, this project imports the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data and allow users to add, update, and view squirrel data. 
## Authors
Group49：Yaliang Lin, Miaoran Lei
## UNIs
yl4597, ml4554
## Main Features
### Management commands
Import: A command that can be used to import the data from the 2018 census file.
Export: A command that can be used to export the data in CSV format.
### Views
#### View sightings on a map
It shows a map that displays the location of the squirrel sightings on an OpenStreets map.
> It is located at: /map
#### View all sightings
It lists all squirrel sightings with links to view each sighting.
> It is located at: /sightings
#### Update a particular sighting
It allows users to update a particular sighting.
> It is located at: /sightings/<unique-squirrel-id>
#### Create a new sighting
It allows users to create a new sighting.
> It is located at: /sightings/add
#### View general statistics
It shows general stats about the sightings. We also visualized the stats in this page.
> It is located at /sightings/stats
## Server Link
We used nginx-uwsgi-django to build the web:
http://squirrels.icu
