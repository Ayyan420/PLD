from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import re_path as url
from django.views.static import serve


urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.home , name = "Home"),
    path('plants-collection', views.plants_collection , name = "Plants Collection"),
    path('about-us', views.about_us , name = "About Us"),
    path('contact-us', views.contact_us , name = "Contact Us"),
    path('prediction-result', views.prediction_result , name = "Prediction Result"),
    path('health', views.health , name = "Health"),
]