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


# def homeview(request):
#     images=Home.objects.all()
#     slide=Home_features.objects.all()
#     allProd=[]
#     catprods=Home_features.objects.values('idd','tittle','photo')
#     cats={item["idd"] for item in catprods}
#     for cat in cats:
#         prod=Home_features.objects.filter(idd=cat)
#         allProd.append(prod)

#     params={'allProd':allProd}
#     return render(request,"home.html",params)

# class AboutPageView(ListView):
#     model = About
#     template_name = 'home_page/about.html'


# class HomeView(ListView):
#     model = Home
#     template_name = 'home_page/studentlife.html'
    
def image_view(request):
    images=Studentlife.objects.all()
    n=len(images)
    nslides=n//4+ceil((n/4)-(n//4))
    dict={'no of slides':nslides,'range':range(1,nslides),'images':images}
    return render(request,'home_page/studentlife.html',context=dict)

# class StudentlifeView(View):
#     model = Studentlife

def aboutview(request):
    pics=About.objects.all()
    dict={'about':pics}
    return render(request,'home_page/about.html',context=dict)