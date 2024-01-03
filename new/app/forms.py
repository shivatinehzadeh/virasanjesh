from django.forms import ModelForm
from django import forms
from .models import contact

class contactForm(ModelForm):
 name = forms.CharField(label='نام\n', label_suffix="",widget=forms.TextInput(attrs={'size':18}))
 email = forms.EmailField(label='ایمیل\n', label_suffix="",widget=forms.TextInput(attrs={'size':18}))
 subject = forms.CharField(label='موضوع \n', label_suffix="",widget=forms.TextInput(attrs={'size':18}))
 پیام =forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":25}))


 class Meta:

     model = contact
     fields = '__all__'