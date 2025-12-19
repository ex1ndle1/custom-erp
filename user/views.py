from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from random import randint


def register(request):
   varification = randint(12222,99999)
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         name = form.cleaned_data['name']
         send_mail(

message=f"your varification code is {varification}",
subject= f'Varification to {name}',
from_email=form.cleaned_data['email'],
recipient_list= ['muzaffarilxomjonov@gmail.com'] ,
fail_silently=False         


         )
         
         return render(request, "user/register.html", {"form": form,"code_sent": True})
      
   else:
     form = UserRegisterForm()

   return render(request , 'user/register.html', {'form':form})   