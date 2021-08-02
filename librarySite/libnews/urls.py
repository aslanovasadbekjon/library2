from django.urls import path
from .views import *
urlpatterns = [
 
    path('',index, name= 'home'),
    path('bolim/<int:bolim_id>/',get_bolim, name='bolim'),
]
