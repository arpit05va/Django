from django import views
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('crops', views.all_crops,name="list-crop"),
    path('add_crop',views.addcrop,name="addcrop"),
    path('add_growplan',views.addgrowplan,name="addgrowplan"),
    path('add_metricplan', views.addmetricplan, name="addmetricplan"),
    path('add_qualityplan', views.addqualityplan, name="addqualityplan"),
    path('crop_table', views.listcrop, name="listcrop"),
    path('show_crop/<id>', views.showcrop, name='showcrop'),
    path('search_crop', views.search_crop, name='searchcrop'),
    path('update_crop/<id>', views.updatecrop, name='updatecrop'),
    path('delete_crop/<id>', views.deletecrop, name='deletecrop'),

]
