
from django.http import HttpResponse
from django.shortcuts import render

from .models import Obyekt, Bolim

def index(request):
	libnews = Obyekt.objects.all()
	bolim = Bolim.objects.all()
	context = {
	'libnews':libnews,
	'title':"Kitoblar olami",
	'bolim': bolim,
	
	}
	return render(request,template_name= 'libnews/index.html',context=context)

def get_bolim(request,bolim_id):
	libnews = Obyekt.filter(bolim_id=bolim_id)
	bolimlar=Bolim.objects.all()
	bolim = Bolim.objects.get(pk=bolim_id)
	context={
	'libnews': libnews,
	'bolimlar':bolimlar,
	'bolim':bolim,
	}
	return render(request, template_name='libnews/index.html',context=context)