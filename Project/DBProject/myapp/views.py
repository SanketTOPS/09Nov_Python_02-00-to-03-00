from django.shortcuts import render,redirect
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

def deletedata(request,id):
    stid=Studinfo.objects.get(id=id)
    Studinfo.delete(stid)
    return redirect('showdata')

def updatedata(request,id):
    stid=Studinfo.objects.get(id=id)
    if request.method=='POST':
        form=Studform(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'updatedata.html',{'stid':stid})