from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Home,Studentlife,Home_features,About,Home_facility
from django.views.generic import TemplateView, ListView, CreateView,View
from math import ceil
from django.core.mail import send_mail, BadHeaderError

def homeview(request):
    images=Home.objects.all()
    slide=Home_features.objects.all()
    facility=Home_facility.objects.all()
    dict={'images':images, 'slide':slide, 'facility':facility}
    return render(request,'home.html',context=dict)

    
def image_view(request):
    images=Studentlife.objects.all()
    n=len(images)
    nslides=n//4+ceil((n/4)-(n//4))
    dict={'no of slides':nslides,'range':range(1,nslides),'images':images}
    return render(request,'home_page/studentlife.html',context=dict)



def aboutview(request):
    pics=About.objects.all()
    dict={'about':pics}
    return render(request,'home_page/about.html',context=dict)