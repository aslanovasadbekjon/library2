

from django.shortcuts import render,get_object_or_404,redirect
from .forms import ObyektForm
from .models import Obyekt, Bolim
from django.views.generic import ListView

# def index(request):
# 	libnews = Obyekt.objects.all()
# 	# bolimlar = Bolim.objects.all()
# 	context = { 
# 	'libnews':libnews,
# 	'title':"Kitoblar olami",
# 	# 'bolimlar': bolimlar,
	
# 	}
# 	return render(request,template_name= 'libnews/index.html',context=context)

def get_bolim(request,bolim_id):
	libnews = Obyekt.objects.filter(bolim_id=bolim_id)
	bolimlar=Bolim.objects.all()
	bolim = Bolim.objects.get(pk=bolim_id)
	return render(request,'libnews/bolim.html',{'libnews':libnews, 'bolimlar':bolimlar,'bolim':bolim})

def view_libnews(request, libnews_id):
	# libnews_item = Obyekt.objects.get(pk=libnews_id)
	libnews_item = get_object_or_404(Obyekt,pk=libnews_id)
	return render(request, 'libnews/view_libnews.html', {'libnews_item': libnews_item})

def add_libnews(request):
	if request.method  ==  'POST': 
		form = ObyektForm(request.POST)
		if form.is_valid():
			#print(form.cleaned_data) 
			#Obyekt.objects.create(**form.cleaned_data)
			form.save()
			#return redirect('add_libnews')
		return render(request, 'libnews/add_libnews.html', {'form':form})
	else:
		form = ObyektForm()
	return render(request, 'libnews/add_libnews.html', {'form':form}) 	

class BoshLibnews(ListView):
	model = Obyekt
	template_name = 'libnews/obyekt_list.html'
	context_object_name = 'libnews'
	#extra_context = {'title':'Bosh sahifa'} 

	def get_context_data(self,*,obyekt_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Bosh sahifa'
		return context

	def get_queryset(self):
		return Obyekt.objects.filter(bolim_id = self.kwargs['bolim_id'],is_published = True)


class LibnewsByCategory(ListView):
	model = Obyekt
	template_name = 'libnews/obyekt_list.html'
	context_object_name = 'libnews'