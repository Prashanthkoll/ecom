from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.models import Products,Buy,Addcard
from django.http import JsonResponse
from django.template.loader import render_to_string
# # Create your views here.
# task for using change implemtn
@login_required(login_url='login_')
def home(request):
    count=Addcard.objects.count()
    products = Products.objects.all()  
    return render(request,'home.html',{'products': products,'count':count})



def addcard(request,id):
    if id:
        a=Products.objects.get(id=id)
        m=Addcard.objects.filter(name=a.name).first()
        if not m:
            Addcard.objects.create(name=a.name,desc=a.desc,img=a.img,cost=a.cost)
        else:
            m.quantity+=1
            m.save()
    c = Addcard.objects.all()
    count=Addcard.objects.count()
    # return render(request, 'addcard.html', {'products': c,'count':count})
    return redirect('home')


def Add(request):
    c = Addcard.objects.all()
    count=Addcard.objects.count()
    a = Buy.objects.all()
    ttcost=sum(i.cost*i.quantity for i in c)
    totalcost=sum(i.cost*i.quantity for i in a)
    return render(request, 'addcard.html',{'products': c,'count':count,'buyproducts': a,'totalcost':totalcost,'ttcost':ttcost})


def Remove(request,id):
    a=Addcard.objects.get(id=id)
    a.delete()
    return redirect('add1')

def Buyproduct(request,id):
    if id:
        a=Addcard.objects.get(id=id)
        m=Buy.objects.filter(name=a.name).first()
        if not m:
            Buy.objects.create(name=a.name,desc=a.desc,img=a.img,cost=a.cost,quantity=a.quantity)
    return redirect('add1')

def ByeDelete(request,id):
    a=Buy.objects.get(id=id)
    a.delete()
    return redirect('add1')

def ByeDeleteAll(request):
    a=Buy.objects.all()
    if request.method=="POST":
        del_value=request.POST['del']
        if del_value:
            a.delete()
        return redirect('add1') 
    return render(request,'conform.html')

def Reduce(request,id):
    a=Addcard.objects.get(id=id)
    if a.quantity==1:
        a.delete()
    else:
        a.quantity-=1
        a.save() 
    return redirect('add1')
def Increse(request,id):
    a=Addcard.objects.get(id=id)
    a.quantity+=1
    a.save() 
    return redirect('add1')
def Reduce1(request,id):
    a=Buy.objects.get(id=id)
    if a.quantity==1:
        a.delete()
    else:
        a.quantity-=1
        a.save() 
    return redirect('add1')
def Increse1(request,id):
    a=Buy.objects.get(id=id)
    a.quantity+=1
    a.save() 
    return redirect('add1')