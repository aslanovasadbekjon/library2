from django.urls import path
from .views import *
urlpatterns = [
 
    #path('',index, name= 'home'),
    path('',BoshLibnews.as_view(), name = 'home'),
    path('bolim/<int:bolim_id>/',get_bolim, name='bolim'),
    path('libnews/<int:libnews_id>/',view_libnews, name='view_libnews'),
    path('libnews/add_libnews/', add_libnews, name='add_libnews'), 
]


