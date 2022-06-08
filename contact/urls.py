from django.urls import re_path as url
from contact import views
app_name='contact'
urlpatterns = [
   
    url(r'^contact/',views.contact, name='contact'),
]