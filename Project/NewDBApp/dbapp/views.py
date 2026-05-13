from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    data=Userinfo.objects.all()
    return render(request,'index.html',{'data':data})

def insert(request):
    if request.method=='POST':
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            print("Resord Inserted!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'insert.html')

def update(request,id):
    stid=Userinfo.objects.get(id=id)
    if request.method=='POST':
        form=Userform(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Resord Updated!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'update.html',{'stid':stid})

def delete(request,id):
    stid=Userinfo.objects.get(id=id)
    Userinfo.delete(stid)
    return redirect('/')
    
    