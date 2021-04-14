import random
import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django.db.models import Sum, Count
from .models import biaoge
from .forms import SquirrelForm
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import View

def map(request):
    targets_for_shown = []
    targets_100 = random.sample(list(biaoge.objects.all()),100)
    for item in targets_100:
        targets_for_shown.append({'xx':item.xx, 'yy':item.yy})
    # define the context
    context = {'sightings':targets_for_shown}
    return render(request, 'htmls/map.html',context)
    
def success(request):

    return render(request,'htmls/success.html')

def mainmenu(request):
    act_options = ['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks', 'Quaas', 'Moans', 'Other activities','Approaches','Tail Twitches','Runs from','Nothing']
    squirrels = biaoge.objects.filter(have_image = True)
    context ={'squirrels':squirrels,
              'activities': act_options,
              'img1':'img1.PNG',
              'img2':'img2.PNG',
              'img3':'img3.JPG',
              'img4':'img4.PNG',
    }
    return render(request,'htmls/mainbase.html', context)

def add(request):
    # see if it is submitted via POST; if yes, load things from web
    if request.method == "POST":
        create_1 = biaoge.objects.create(
        xx = request.POST.get('latitude', 0),
        yy = request.POST.get('longtitude', 0),
        Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID', 00-0000-00-00),
        shift = request.POST.get('shift', None),
        date = request.POST.get('date', None),
        age = request.POST.get('age', None),
        primary_fur_color = request.POST.get('primary_fur_color', None),
        location = request.POST.get('location', None),
        specific_location = request.POST.get('specific_location', None),
        running = request.POST.get('running', False),
        chasing = request.POST.get('chasing', False),
        climbing = request.POST.get('climbing', False),
        eating = request.POST.get('eating', False),
        foraging = request.POST.get('foraging', False),
        other_activities = request.POST.get('other_activities', None),
        kuks = request.POST.get('kuks', False),
        quaas = request.POST.get('quaas', False),
        tail_flags = request.POST.get('tail_flags', False),
        tail_twitches = request.POST.get('tail_twitches', False),
        approaches = request.POST.get('approaches', False),
        indifferent = request.POST.get('indifferent', False),
        runs_from = request.POST.get('runs_from', False),
        moans = request.POST.get('moans', False),
        profile_image = request.FILES.get('profile_image', None),
        have_image = request.POST.get('have_image', False),
        )
        create_1.save()
        return redirect(f'/success')
    else:
        context= {'sssss':'sssss.jpg'}
        return render(request, 'htmls/add.html', context)

def edit(request, squirrel_id):
    create_2 = biaoge.objects.get(pk = squirrel_id)
    if request.method == "POST":
        create_2.xx = request.POST.get('latitude', 0)
        create_2.yy = request.POST.get('longtitude', 0)
        create_2.Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID', 00-00-0000-00)
        create_2.shift = request.POST.get('shift', None)
        create_2.date = request.POST.get('date', 1000-10-10)
        create_2.age = request.POST.get('age', None)
        create_2.primary_fur_color = request.POST.get('primary_fur_color', None)
        create_2.location = request.POST.get('location',None)
        create_2.specific_location = request.POST.get('specific_location', None)
        create_2.other_activities = request.POST.get('other_activities',None)
        create_2.running = request.POST.get('running', False)
        create_2.chasing = request.POST.get('chasing', False)
        create_2.climbing = request.POST.get('climbing', False)
        create_2.eating = request.POST.get('eating', False)
        create_2.foraging = request.POST.get('foraging', False)
        create_2.kuks = request.POST.get('kuks', False)
        create_2.quaas = request.POST.get('quaas', False)
        create_2.tail_flags = request.POST.get('tail_flags', False)
        create_2.tail_twitches = request.POST.get('tail_twitches', False)
        create_2.approaches = request.POST.get('approaches', False)
        create_2.indifferent = request.POST.get('indifferent', False)
        create_2.runs_from = request.POST.get('runs_from', False)
        create_2.moans = request.POST.get('moans', False)
        create_2.have_image = request.POST.get('have_image', False)
        if request.FILES.get('profile_image', None):
            create_2.profile_image = request.FILES.get('profile_image', None)
        create_2.save()
        
        return redirect(f'/success')
    else:
        context = {'squirrels':create_2, 'method':'POST', 'sssss': 'sssss.jpg'}
        return render(request, 'htmls/edit.html', context)

def search(request):
    squirrel_id = request.GET.get('search')
    try:
        squirrels = biaoge.objects.get(pk = squirrel_id)
    except:
        return render(request, 'htmls/busuccess.html')
    else:
        squirrels = biaoge.objects.get(pk = squirrel_id)
        context= {'squirrels': squirrels, 'sssss':'sssss.jpg'}
        return render(request, 'htmls/edit.html', context)

def sightings(request):
    squirrels = biaoge.objects.order_by('Unique_Squirrel_ID')
    sightings_all = biaoge.objects.all()
    context = {'squirrels': squirrels}
    return render(request,'htmls/sightings.html', context)

def stats(request):

    sightings_all = biaoge.objects.all()

    Juv_prop = sightings_all.filter(age = 'Juvenile').count() / (sightings_all.filter(age = 'Juvenile').count() + sightings_all.filter(age = 'Adult').count())
    Juv_prop = "{:.2%}".format(Juv_prop)
    Adu_prop = sightings_all.filter(age = 'Adult').count() / (sightings_all.filter(age = 'Juvenile').count() + sightings_all.filter(age = 'Adult').count())
    Adu_prop = "{:.2%}".format(Adu_prop)
 
    AM_prop = sightings_all.filter(shift = 'AM').count() / (sightings_all.filter(shift = 'AM').count() + sightings_all.filter(shift = 'PM').count())
    AM_prop = "{:.2%}".format(AM_prop)
    PM_prop = sightings_all.filter(shift = 'PM').count() / (sightings_all.filter(shift = 'AM').count() + sightings_all.filter(shift = 'PM').count())
    PM_prop = "{:.2%}".format(PM_prop)
    
    Total_color = sightings_all.filter(primary_fur_color = 'Black').count() + sightings_all.filter(primary_fur_color = 'Gray').count() + sightings_all.filter(primary_fur_color = 'Cinnamon').count()
    Gray_prop = sightings_all.filter(primary_fur_color = 'Gray').count() / (Total_color)
    Gray_prop = "{:.2%}".format(Gray_prop)
    Black_prop = sightings_all.filter(primary_fur_color = 'Black').count() / (Total_color)
    Black_prop = "{:.2%}".format(Black_prop)
    Cinnamon_prop = sightings_all.filter(primary_fur_color = 'Cinnamon').count() / (Total_color)
    Cinnamon_prop = "{:.2%}".format(Cinnamon_prop)

    Above_Ground_prop = sightings_all.filter(location = 'Above Ground').count() / (sightings_all.filter(location = 'Above Ground').count() + sightings_all.filter(location = 'Ground Plane').count())
    Above_Ground_prop = "{:.2%}".format(Above_Ground_prop)
    Ground_Plane_prop = sightings_all.filter(location = 'Ground Plane').count() / (sightings_all.filter(location = 'Above Ground').count() + sightings_all.filter(location = 'Ground Plane').count())
    Ground_Plane_prop= "{:.2%}".format(Ground_Plane_prop)

    Run_from_true_prop = sightings_all.filter(runs_from = True).count() / (sightings_all.filter(runs_from = True).count() + sightings_all.filter(runs_from = False).count())
    Run_from_true_prop = "{:.2%}".format(Run_from_true_prop)
    Run_from_false_prop = sightings_all.filter(runs_from = False).count() / (sightings_all.filter(runs_from = True).count() + sightings_all.filter(runs_from = False).count())
    Run_from_false_prop = "{:.2%}".format(Run_from_false_prop)

    foraging_num = sightings_all.filter(foraging=True).count()
    eating_num = sightings_all.filter(eating=True).count()
    climbing_num = sightings_all.filter(climbing=True).count()
    chasing_num = sightings_all.filter(chasing=True).count()
    running_num = sightings_all.filter(running=True).count()
    total_movements = foraging_num + eating_num + climbing_num + chasing_num + running_num
    foraging_prop = "{:.2%}".format(foraging_num / total_movements)
    eating_prop = "{:.2%}".format(eating_num / total_movements)
    chasing_prop = "{:.2%}".format(chasing_num / total_movements)
    running_prop = "{:.2%}".format(running_num / total_movements)
    climbing_prop = "{:.2%}".format(climbing_num / total_movements)

    AM_num = sightings_all.filter(shift = 'AM').count()
    PM_num = sightings_all.filter(shift = 'PM').count()
    Juvenile_num = sightings_all.filter(age = 'Juvenile').count()
    Adult_num = sightings_all.filter(age = 'Adult').count()
    Black_num = sightings_all.filter(primary_fur_color = 'Black').count()
    Gray_num = sightings_all.filter(primary_fur_color = 'Gray').count()
    Cinnamon_num = sightings_all.filter(primary_fur_color = 'Cinnamon').count()
    Above_Ground_num = sightings_all.filter(location ='Above Ground').count()
    Ground_Plane_num = sightings_all.filter(location = 'Ground Plane').count()
    Run_from_true = sightings_all.filter(runs_from = True).count()
    Run_from_false = sightings_all.filter(runs_from = False).count()
    foraging_num = sightings_all.filter(foraging=True).count()
    eating_num = sightings_all.filter(eating = True).count()
    climbing_num = sightings_all.filter(climbing = True).count()
    chasing_num = sightings_all.filter(chasing = True).count()
    running_num = sightings_all.filter(running = True).count()

    context = {
            'Total':sightings_all.count(),
            'Runs_From': {'True':Run_from_true, 'False':Run_from_false},
            'Runs_From_pct': {'True':Run_from_true_prop, 'False':Run_from_false_prop},
            'Shift': {'AM': AM_num,'PM': PM_num},
            'Shift_pct': {'AM': AM_prop,'PM': PM_prop},
            'Age': {'Juvenile': Juvenile_num, 'Adult': Adult_num},
            'Age_pct': {'Juvenile': Juv_prop, 'Adult': Adu_prop},
            'Primary_Fur_Color': {'Black':Black_num, 'Gray':Gray_num, 'Cinnamon':Cinnamon_num},
            'Primary_Fur_Color_pct': {'Black':Black_prop, 'Gray':Gray_prop, 'Cinnamon':Cinnamon_prop},
            #'Activities':{'foraging':foraging_num, 'eating':eating_num, 'climbing': climbing_num},
            #'Activities_pct': {'foraging':foraging_prop, 'eating':eating_prop, 'climbing': climbing_prop},
            'Location': {'Above_Ground':Above_Ground_num, 'Ground_Plane':Ground_Plane_num},
            'Location_pct': {'Above_Ground':Above_Ground_prop, 'Ground_Plane':Ground_Plane_prop},
            }

    return render(request, 'htmls/stats.html', {'context':context})

def mainmenu(request):
    squirrels = biaoge.objects.filter(have_image = True)
    activities = ['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks', 'Quaas', 'Moans', 'Other activities','Approaches','Tail Twitches','Runs from','Nothing']
    context ={'squirrels':squirrels,
              'activities': activities,
              'img1':'img1.PNG',
              'img2':'img2.PNG',
              'img3':'img3.JPG',
              'img4':'img4.PNG',
    }
    return render(request,'htmls/mainbase.html',context)


    def sightings(request):
    squirrels = biaoge.objects.order_by('Unique_Squirrel_ID')
    context = {'squirrels':squirrels,}
    return render(request,'htmls/sightings.html',context)