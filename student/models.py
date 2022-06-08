from __future__ import unicode_literals
import os
from django.db import models
#This resolves url
from django.urls import reverse
import datetime
from company.models import Job_desc


# Create your models here.

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.s_username, ext)
    return os.path.join('documents/', filename)

# import hashlib

# user = User()
# user.id
# user.user_name
# user.password_hash -> H(x) = 64/32/128 character unique string
# user.email
# user.contact
# user.user_type -> {'Student', 'Company'}

# # password change request
# request = {
#     "student_id": student.id,
#     "user_name": user.name,
#     "new_pass": <whatever_the_user_has_entered>,
#     "confirm_new_pass":  <whatever_the_user_has_entered>
# }

# user = User.objects.get(username=request["user_name"])

# if request["new_pass"] == request["confirm_new_pass"]:
#     new_password = request["new_pass"]
#     user.password_hash = hashlib.md5(new_password)

# student = Student()
# student.id
# student.s_first_name
# student.s_last_name

# company = Company()
# .
# .


class StudentDB(models.Model):
    COURSE=(
        ('UG','Bachelors'),
        ('PG','Masters'),
        ('PHD','Philospher'),
    )
    BRANCH=(
        ('FE','Front-End'),
        ('BE','Back-End'),
        ('P','Programming'),
    )
    s_username = models.CharField(max_length=250, default='')
    s_name = models.CharField(max_length=250,blank=True)
    s_password = models.CharField(max_length=250, blank=True)
    s_confirm_password=models.CharField(max_length=250, blank=True)
    dob = models.DateField()
    emailid = models.EmailField(blank=True)
    branch = models.CharField(max_length=10,choices=BRANCH, default='P') #search for creating drop down menu
    course =  models.CharField(max_length=5,choices=COURSE, default='PG')#search for drop down MTech Btech
    s_verified = models.BooleanField(default=False, blank=True)
    s_verification = models.IntegerField(default=0, blank=True)
    contactno = models.CharField (max_length=20,blank=True)
    resume = models.FileField(upload_to=content_file_name, blank=True)
    #address = models.CharField (max_length=500)    
    #profile_pic = models.FileField();

    def __str__(self):
        return str(self.s_username)


class Edit_Details(models.Model):
    #s_perm  = models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=250, blank=True, null=True)
    emailid = models.EmailField(blank=True)
    qualification=models.CharField(max_length=250,blank=True, null=True)
    resume=models.FileField(upload_to="documents/",blank=True)

    def __str__(self):
        return self.s_name

class Notifications(models.Model):
    jobid = models.ForeignKey(Job_desc, on_delete=models.CASCADE,null=True)
    n_text=models.CharField(max_length=250,null=True)
    old=models.BooleanField(default=True)
    stdid=models.ForeignKey(StudentDB,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.n_text)

class AppliedJob(models.Model):
    jobid= models.ForeignKey(Job_desc, on_delete=models.CASCADE,null=True)
    stdid=models.ForeignKey(StudentDB,on_delete=models.CASCADE,null=True)
    applied=models.BooleanField(default=False)
    got_offer=models.CharField(max_length=250,default="No")
    def __str__(self):
        return str(self.got_offer)