from django.shortcuts import render
from .forms import contactForm
from .models import contact
from django.http import HttpResponseRedirect
from .models import resume
# Create your views here.

def base(request):
 Resume=resume.objects.all()
 return render(request,'index.html',{'Resume':Resume})

def about(request):

   return render(request, 'about_us.html')


def contactUs(request):
 Resume=resume.objects.all()

 if request.method == 'POST':
  form = contactForm(request.POST)
  if form.is_valid():
   cd = form.cleaned_data

  return HttpResponseRedirect('contact.html',{'form':form})
 else:

  form = contactForm()

  if 'submitted' in request.GET:

    submitted = True

  return render(request,'contact.html',{'form':form})
