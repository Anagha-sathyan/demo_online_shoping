from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import ModeForm
from . models import shop

# Create your views here.
def fun(request):
    product=shop.objects.all()
    return render(request,"home.html",{'products':product})

def details(request,shop_id):
    product1=shop.objects.get(id=shop_id)
    return render(request,'details.html',{'product':product1})

def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        img = request.FILES['img']
        price=request.POST.get('price')
        var=shop(name=name,desc=desc,price=price,img=img)
        var.save()
        print("product added")
    return render(request,"add_product.html")

def update(request,id):
    obj=shop.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        print("updated")
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method=='POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html' )