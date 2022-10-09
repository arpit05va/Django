from dataclasses import field
from django import forms
from django.forms import ModelForm 
from .models import Crops
from .models import GrowPlan
from .models import QualityPlan
from .models import MetricPlan


# create a Crops Form
class CropForm(ModelForm):
    class Meta:
        model=Crops
        fields = ('name', 'desc' ,'type')
        labels={
            'name':'name of crop',
            'desc':'Description about crop',
            'type':'Type of Crop',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Mango'}),
            'desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Info About Mango'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fruit'})
        }

# create a Grow Plan
class GrowPlanForm(ModelForm):
    class Meta:
        model = GrowPlan
        fields = ('name', 'desc' ,'date' ,'qualityplan' ,'crop')
        labels = {
            'name': 'Name',
            'desc': 'Description',
            'date': 'Date',
            'qualityplan':'Quality Plan',
            'crop':'Crop Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(format=('%d-%m-%y'), attrs={'class': 'form-control', 'placeholder': 'DD-MM-YY', 'type': 'date'}),
            'qualityplan': forms.Select(attrs={'class': 'form-select'}),
            'crop': forms.Select(attrs={'class': 'form-select'})

        }


# create a Quality Form
class QualityPlanForm(ModelForm):
    class Meta:
        model = QualityPlan
        fields = ('name' ,'desc' ,'metricplan')
        labels = {
            'name': 'Name',
            'desc': 'Description',
            'metricplan': 'Metricplan',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.SelectMultiple(attrs={'class': 'form-select'})
        }

# create a MetricPlan Form


class MetricPlanForm(ModelForm):
    class Meta:
        model = MetricPlan
        fields = ('name', 'desc', 'type', 'value', 'start_day', 'end_day')
        labels = {
            'name': 'name of crop',
            'desc': 'Description about crop',
            'type': 'Type of Crop',
            'value':'Value',
            'start_day':'Start Day',
            'end_day':'End Day'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_day': forms.DateInput(format=('%d-%m-%y'), attrs={'class': 'form-control', 'placeholder': 'DD-MM-YY',  'type': 'date'}),
            'end_day': forms.DateInput(format=('%d-%m-%y'), attrs={'class': 'form-control', 'placeholder': 'DD-MM-YY', 'type': 'date'}),
        }

