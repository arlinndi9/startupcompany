from django.contrib import messages
from django.shortcuts import render,redirect
from .models import  Contact, Jobs, Stories, apply_job, Team
from .form import ContactForm, apply_job, Contact
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def stories(request):
    stories=Stories.objects.all()
    data={
        'stories':stories
    }
    return render(request,'stories.html',data)

def about(request):
    team=Team.objects.all()
    data={
        'team':team
    }
    return render(request,'about.html',data)


def career(request):
    jobs=Jobs.objects.all()
    data={
        'jobs':jobs
    }
    return render(request,'careers.html',data)

def career_apply(request):
    jobs=Jobs.objects.all()
    if request.method == "POST":
        form=apply_job(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aplikimi juaj u dergua me sukses!Do ju kontaktojme se shpejti!')

    return render(request,'apply.html',{'form':apply_job,'jobs':jobs})

def contact(request):
     if request.method=="POST":
         form=Contact(request.POST)
         if form.is_valid():
             form.save()
             messages.success(request, 'Mesazhi juaj u dergua me sukses!Do ju kontaktojme se shpejti!')
     return render(request,'contact.html',{'form':Contact})
# Create your views here.

