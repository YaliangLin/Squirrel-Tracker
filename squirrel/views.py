import random
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django.db.models import Sum, Count
from .models import biaoge
import datetime
import json
from .forms import SquirrelForm
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import View

def map(request):
    list_s = []
    First_100_sightings = random.sample( list (biaoge.objects.all()), 100)
    for sighting in First_100_sightings:
        list_s.append({'xx':sighting.xx, 'yy':sighting.yy})
    context = {'sightings':list_s, }

    return render(request,'htmls/map.html', context)
    

