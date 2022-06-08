from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.


def home(request):
    return render(request, 'student/student_login.html')

def index(request):
    return render(request, 'home/index.html')

# def contact(request):
#     return render(request, 'home/contact.html')

