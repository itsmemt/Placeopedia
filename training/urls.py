from django.urls import re_path as url
from . import views  #Here dot indicates current file   
app_name='training'
urlpatterns = [
   
    url('training/',views.training, name='training'),
]