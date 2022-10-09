from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Crops
from .models import GrowPlan
from .models import QualityPlan
from .models import MetricPlan
from .forms import CropForm
from .forms import GrowPlanForm
from .forms import MetricPlanForm
from .forms import QualityPlanForm


def deletecrop(request, id):
    deletec = Crops.objects.get(pk=id)
    deletec.delete()
    return redirect('listcrop')

def updatecrop(request,id):
    update = Crops.objects.get(pk=id)
    form = CropForm(request.POST or None,instance=update)
    if form.is_valid():
        form.save()
        return redirect('listcrop')
    return render(request, 'api/update_crop.html', {'update': update,'form':form})

def showcrop(request,id):
    crop = Crops.objects.get(pk=id)
    return render(request, 'api/showcropdetails.html', {'crop': crop})

def listcrop(request):
    crop_list = Crops.objects.all()
    return render(request, 'api/croptabel.html', {'crop_list': crop_list})

def search_crop (request):
    if request.method == "POST":
        searched=request.POST['searched']
        crops=Crops.objects.filter(name__contains=searched)
        return render(request, 'api/search_crop.html', {'searched': searched, 'crops': crops})
    else:
        return render(request, 'api/search_crop.html', {})

    

def addcrop(request):
    submitted=False
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            owner=form.save(commit=False)
            owner.user=request.user.id
            owner.save()
            # form.save()
            return HttpResponseRedirect('/add_crop?submitted=True')
    else:
        form = CropForm
        if 'submitted' in request.GET:
            submitted=True
    
    return render(request, 'api/add_crops.html', {'form':form,'submitted':submitted})


def addgrowplan(request):
    submitted = False
    if request.method == "POST":
        form = GrowPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_growplan?submitted=True')
    else:
        form = GrowPlanForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'api/add_growplan.html', {'form': form, 'submitted': submitted})


def addmetricplan(request):
    submitted = False
    if request.method == "POST":
        form = MetricPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_metricplan?submitted=True')
    else:
        form = MetricPlanForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'api/add_metricplan.html', {'form': form, 'submitted': submitted})


def addqualityplan(request):
    submitted = False
    if request.method == "POST":
        form = QualityPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_qualityplan?submitted=True')
    else:
        form = QualityPlanForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'api/add_qualityplan.html', {'form': form, 'submitted': submitted})




def all_crops(request):
    crop_list=Crops.objects.all()
    return render(request,'api/crop_list.html',{'crop_list':crop_list})



def home(request):
    return render(request,'api/home.html',{})
