from django.contrib import admin
# Here we are importing models from models
from .models import StudentDB,Notifications,AppliedJob
# Register your models here.
admin.site.register(StudentDB)
admin.site.register(Notifications)
admin.site.register(AppliedJob)
