from django.urls import path,include
from . import views

app_name='home_page'
urlpatterns = [
    path('',views.homeview,name='home'),
    
    path('studentlife/',views.image_view,name='studentlife'),
    
    path('about/',views.aboutview,name='about')
]
