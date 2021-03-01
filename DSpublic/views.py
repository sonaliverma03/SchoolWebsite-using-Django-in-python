from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render,redirect

# class HomePage(TemplateView):
#     template_name='home.html'

# class ContactPage(TemplateView):
#     template_name='contact.html'

def contactView(request):
    if request.method == 'POST':
        name=request.POST['Name']
        email=request.POST['Email']
        message=request.POST['Message']
        
        send_mail(
            name,
            email,
            message,
            ['sonaliverma1103@gmail.com']
            )
        
        return render(request, "contact.html", {'name': name})
    else:
        return render(request, "contact.html", {})