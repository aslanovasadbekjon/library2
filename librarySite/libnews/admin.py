from django.contrib import admin
from libnews.views import Obyekt

# Register your models here.
from .models import Obyekt,Bolim

class ObyektAdmin(admin.ModelAdmin):
	list_display = ('id','title','aftor','tavsif','bolim','created_at','nashri','photo','is_published')
	list_display_links = ('id','title')
	search_fields = ('title','aftor')
	list_filter = ('is_published','bolim')
	list_editable = ('bolim','photo')

class BolimAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('id','title')
	search_fields = ('title')


admin.site.register(Obyekt,ObyektAdmin)
admin.site.register(Bolim)