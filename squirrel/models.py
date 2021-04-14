from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class biaoge(models.Model):
    # coordinates
    xx = models.FloatField (help_text = ('Latitude'), null = True)
    yy = models.FloatField (help_text = ('Longtitude'), null = True)

    # ID
    Unique_Squirrel_ID = models.CharField(max_length = 100, help_text = ('The Unique Squirrel ID'), unique = True, primary_key = True)

    # age
    ADULT, JUVENILE = 'Adult', 'Juvenile'
    AGE_CHOICES = ((ADULT,'Adult'), (JUVENILE,'Juvenile'))
    age = models.CharField(max_length = 100, help_text = ('Age'), choices = AGE_CHOICES, null = True)

    # shift
    PM, AM = 'PM', 'AM'
    SHIFT_CHOICES = ((PM,'PM'), (AM,'AM'))
    shift = models.CharField(max_length = 100, default='', help_text = ('Shift'), choices = SHIFT_CHOICES, null = True)
    date = models.DateField(default='1000-10-10', help_text = ('date'), null = True)

    # color
    GRAY, CINNAMON, BLACK = 'Gray', 'Cinnamon', 'Black'
    FUR_COLOR_CHOICES = ((GRAY,'Gray'), (CINNAMON,'Cinnamon'), (BLACK,'Black'))
    primary_fur_color = models.CharField(max_length = 100, help_text = ('Primary Fur Color'), choices = FUR_COLOR_CHOICES, null = True)

    # locations
    GROUND_PLANE, ABOVE_GROUND = 'Ground Plane', 'Above Ground'
    LOCATION_CHOICES = ((GROUND_PLANE,'Ground Plane'),(ABOVE_GROUND,'Above Ground'))
    location = models.CharField(max_length = 100, help_text = ('Location'), choices = LOCATION_CHOICES, null = True)
    specific_location = models.CharField(max_length = 100, help_text = ('Specific Location'), null = True)

    # activities
    foraging = models.BooleanField(help_text = ('Foraging'), default = False)
    climbing = models.BooleanField(help_text = ('Climbing'), default = False)
    eating = models.BooleanField(help_text = ('Eating'), default = False)
    running = models.BooleanField(help_text = ('Running'), default = False)
    chasing = models.BooleanField(help_text = ('Chasing'), default = False)
    other_activities = models.CharField(max_length = 100, help_text = ('Other Activities'), default = '', null = True)

    # others
    kuks = models.BooleanField(help_text = ('Kuks'), default = False)
    quaas = models.BooleanField(help_text = ('Quaas'), default = False)
    tail_twitches = models.BooleanField(help_text = ('Tail Twitches'), default = False)
    tail_flags = models.BooleanField(help_text = ('Tail Flags'), default = False)
    approaches = models.BooleanField(help_text = ('Approaches'), default = False)
    indifferent = models.BooleanField(help_text = ('Indifferent'), default = False)
    runs_from = models.BooleanField(help_text = ('Runs From'), default = False)
    moans = models.BooleanField(help_text= ('Moans'), default = False)
    
    # image
    profile_image = models.ImageField(help_text= ('Profile Picture'), upload_to = "img/", null = True)
    have_image = models.BooleanField(help_text=('Please check it on if there is an image for this squirrel'), default = False)
    
    def __str__(self):
        return self.Unique_Squirrel_ID
