from django import template
from libnews.models import Bolim
register = template.Library()

@register.simple_tag()
def get_bolimlar():
	return Bolim.objects.all()
