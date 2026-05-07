from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        form=Studform(request.POST)
        if form.is_valid():
            form.save()
            print("Record inserted!")
        else:
            print(form.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=Studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})