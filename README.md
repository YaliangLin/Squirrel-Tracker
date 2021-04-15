# E4501 Final Project: Squirrel Tracker

## Introduction
This is the final project of the course E4501 Tools for Analytics. In order to keep track of the squirrels in the Central Park, this project imports the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data and allow users to add, update, and view squirrel data. 
## Group Name and Section
Project Group 49, Section 1
## UNIs
UNIs: [yl4597, ml4554] 
## Server Link
We use nginx-uwsgi-django to build the web. The link is: http://squirrels.icu
## Main Features
[This video](https://b23.tv/3z3KC9) shows the main features of this project. Specific main features are also listed below:
### Management Commands
Import: A command that can be used to import the data from the 2018 census file.    
```
python manage.py import /path/to/file.csv
```
Export: A command that can be used to export the data in CSV format.  
```
python manage.py export /path/to/output.csv
```
### Home Page
It uses the image carousel for switching different pages. Several specific squirrel sightings are also shown in the home page as examples.   

![Gif of Home Page](https://github.com/Miaoran-Lei/Squirrel-Tracker/blob/master/media/img/Completed_Home_Page.gif)
### Views
#### View sightings on a map
It shows a map that displays the location of the squirrel sightings on an OpenStreets map. It is located at: `/map`   
   
![Picture of Map](https://github.com/Miaoran-Lei/Squirrel-Tracker/blob/master/media/img/Completed_Map.PNG)
#### View all sightings
It lists all squirrel sightings with links to view each sighting. It is located at: `/sightings`   
   
![Picture of Sightings](https://github.com/Miaoran-Lei/Squirrel-Tracker/blob/master/media/img/Completed_Sightings.PNG)
#### Update a particular sighting
It allows users to update a particular sighting. It is located at: `/sightings/<unique-squirrel-id>`    
     
![Picture of Update](https://github.com/Miaoran-Lei/Squirrel-Tracker/blob/master/media/img/Completed_Update.PNG)
#### Create a new sighting
It allows users to create a new sighting. It is located at: `/sightings/add`    
   
![Picture of Add](https://github.com/Miaoran-Lei/Squirrel-Tracker/blob/master/media/img/Completed_Add.PNG)
#### View general statistics
It shows general statistics of six attributes about the sightings. The statistics are visualized in this page. It is located at: `/sightings/stats`    
   
![Picture of Stats](https://github.com/Miaoran-Lei/Squirrel-Tracker/blob/master/media/img/Completed_Stats.PNG)

