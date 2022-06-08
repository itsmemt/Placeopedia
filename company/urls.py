from django.urls import re_path as url
from . import views
app_name='company'

urlpatterns = [
    url('signup/', views.post_list, name='signup_page'),
    url('login', views.view_home, name='login_page'),
    url('edit', views.view_edit, name='home_page'),
    url('verify',views.verify,name='verify_page'),
    url('userc/(?P<username>[A-Za-z_0-9]+)/$', views.profile, name='profile'),
    url('jobreqs',views.Jobreqs,name='job_requirements'),
    url('change_password', views.change_password,name='passchg'),
    url('changed', views.successfull_change,name='passchgsucc'),
    url('listjobs',views.listjobs,name='listjobs'),
    url('jobs/(?P<jobid>[0-9]+)/',views.jobdesc,name='jobdesc'),
    url('applied_msg/', views.jobapplied, name='jobapplied'),
    url('student_list/(?P<jobid>[0-9]+)/', views.view_student_list, name='studlist'),
    url('taken_name/', views.already_taken, name="takenc"),
    url('offered/(?P<userid>[A-Za-z_0-9]+)/$', views.offered, name="takenc"),
]