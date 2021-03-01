from django.urls import path,include
from . import views

app_name='home_page'
urlpatterns = [
    # path('',views.HomePageView.as_view(),name='home'),
    path('',views.homeview,name='home'),
    # path('studentlife/',views.StudentlifeView.as_view(),name='studentlife'),
    path('studentlife/',views.image_view,name='studentlife'),
    # path('about/',views.AboutPageView.as_view(),name='about'),
    path('about/',views.aboutview,name='about')
]
