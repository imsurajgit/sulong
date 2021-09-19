
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def socialmedia(request):
    return render(request, 'socialmedia.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your forms has been submitted')
    return render(request, 'contact.html')

    
