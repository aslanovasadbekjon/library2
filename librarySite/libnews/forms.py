from django import forms
from .models import Obyekt
import re
from django.core.exceptions import ValidationError

# class LibnewsForm(forms.Form):
# 	title = forms.CharField(max_length=150, label= "Sarlavha", widget=
# 		forms.TextInput(attrs={"class":"form-control"}))

# 	aftor  = forms.CharField(label= "Mulllif", widget=
# 		forms.TextInput(attrs={"class":"form-control"}))

# 	tavsif = forms.CharField(label = "Tavsif",required=False,  widget=
# 		forms.Textarea(attrs={"class":"form-control"}))

# 	created_at = forms.DateTimeField(label="Yaratilgan vaqti", widget=
# 		forms.SelectDateWidget(attrs={"class":"form-control"}))

# 	nashri = forms.DateTimeField(label= "Nashri(yangilangan vaqti)",  widget=
# 		forms.DateInput(attrs={"class":"form-control"}))

# 	is_published = forms.BooleanField(label="Chop qilinganligi", initial=True)

# 	bolim = forms.ModelChoiceField(label= "Kategoriyasi", empty_label="tanlang",queryset=Bolim.objects.all(), widget=
# 		forms.Select(attrs={"class":"form-control"}))
class ObyektForm(forms.ModelForm):
	class Meta:
		model = Obyekt
		#fields = '__all__'
		fields = ['title', 'aftor','tavsif', 'is_published','bolim']
		widgets = {
		'title' : forms.TextInput(attrs={"class":"form-control"}),
		'aftor' : forms.TextInput(attrs={"class":"form-control"}),
		'tavsif' : forms.Textarea(attrs={"class":"form-control"}),
		'bolim' : forms.Select(attrs={"class":"form-control"})
		}

	def clean_title(self):
		title = self.cleaned_data['title']
		if re.match(r'\d', title):
			raise ValidationError("Sarlavha raqam bilan boshlanmaydi")
		return title			