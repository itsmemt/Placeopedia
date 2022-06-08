from django.urls import re_path as url
# from student import views
from .import views

app_name='home'

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^home/',views.index, name='homepage'),
    # url(r'^contact/',views.contact, name='contact'),
    
]