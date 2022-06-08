from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from home import views


app_name='student'
urlpatterns = [
    #home/ or / or student/
    re_path(r'student_login/$', views.studentlogin, name='student_login'),
    re_path(r'auth/$', views.auth_view ,name='auth'),
    re_path(r'edit_details/$', views.view_edit ,name='edit_page'),
    re_path(r'logout/$',views.logout,name='logout'),
    re_path(r'users/(?P<username>[A-Za-z_0-9]+)/$', views.profile, name='profile'),
#    url(r'loggedin/$',views.loggedin,name='loggedin'),
  #  url(r'invalid/$',views.invalid_login,name='invalid'),
    re_path(r'^home/',views.studentlogin, name='student'),
    re_path(r'^$', views.studentlogin, name='student'),
 #register new student
    re_path(r'register/$', views.studentregistration, name='student_register'),
    re_path(r'listjobs/',views.listjobs,name='list_jobs'),
    re_path(r'changed/', views.successfull_change,name='passchgsucc'),
    re_path(r'change_password/', views.change_password, name='passchg'),
    re_path(r'offer_letter/', views.get_offer, name='offer'),
    re_path(r'success/',views.update_details,name="update"),
    re_path(r'taken_name/',views.already_taken,name="taken"),
    re_path(r'profile/(?P<username>[A-Za-z_0-9]+)/$', views.view_stud_details, name="stud_details"),
    re_path(r'download/', views.download, name="download"),
    re_path(r'resume/(?P<username>[A-Za-z_0-9]+)/$', views.resumed, name="resumed"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
