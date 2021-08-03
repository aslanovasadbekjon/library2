

from django.shortcuts import render,get_object_or_404

from .models import Obyekt, Bolim

def index(request):
	libnews = Obyekt.objects.all()
	# bolimlar = Bolim.objects.all()
	context = {
	'libnews':libnews,
	'title':"Kitoblar olami",
	# 'bolimlar': bolimlar,
	
	}
	return render(request,template_name= 'libnews/index.html',context=context)

def get_bolim(request,bolim_id):
	libnews = Obyekt.objects.filter(bolim_id=bolim_id)
	bolimlar=Bolim.objects.all()
	bolim = Bolim.objects.get(pk=bolim_id)
	return render(request,'libnews/bolim.html',{'libnews':libnews, 'bolimlar':bolimlar,'bolim':bolim})

def view_libnews(request, libnews_id):
	# libnews_item = Obyekt.objects.get(pk=libnews_id)
	libnews_item = get_object_or_404(Obyekt,pk=libnews_id)
	return render(request, 'libnews/view_libnews.html', {'libnews_item': libnews_item})