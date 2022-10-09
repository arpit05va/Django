from django.contrib import admin
from .models import GrowPlan
from .models import Crops
from .models import MetricPlan
from .models import QualityPlan

# Register your models here.
# admin.site.register(GrowPlan)
# admin.site.register(MetricPlan)
admin.site.register(QualityPlan)

@admin.register(Crops)
class CropsAdmin(admin.ModelAdmin):
    list_display=('name','type')
    search_fields=('name','type')

@admin.register(MetricPlan)
class MetricPlanAdmin(admin.ModelAdmin):
    list_display=('name','type','value')


@admin.register(GrowPlan)
class GrowPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'crop')





