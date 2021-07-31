from django.urls import path
from .views import *
urlpatterns = [
 
    path('',index),
    path('bolim/<int:bolim_id>/',get_bolim)
]

