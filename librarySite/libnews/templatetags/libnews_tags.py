from django import template
from libnews.models import Bolim
register = template.Library()

@register.simple_tag(name="get_list_bolimlar")
def get_bolimlar():
	return Bolim.objects.all()

@register.inclusion_tag('libnews/list_bolimlar.html')
def show_bolimlar(arg1='Hello', arg2 = "world"):
	bolimlar=Bolim.objects.all()
	return {'bolimlar': bolimlar, "arg1": arg1, "arg2": arg2 }
	