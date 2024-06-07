from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from supplier.forms import *
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
import string
import random

def index(request):
    return render(request, 'supplier/index.html', {})

def suppliersignup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            form.groups = "Supplier"
            data = users.objects.filter(Q(email=email)|Q(username=username))
            if data.count() > 0:
                messages.error(request,"Error: This Username/Email is not available or used")
            else:
                form.save()
                return redirect("/")
        else:
            form = CustomUserCreationForm(request.POST)
    elif request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "registration/supplier_signup.html",{"form": form})


def supplierdetails(request):
    if request.user.is_authenticated:
        data = users.objects.get(email=request.user.email)
        neworder = order.objects.filter(supplierid=data.username, status="neworder")
        processing = order.objects.filter(supplierid=data.username, status="processing")
        delivering = order.objects.filter(supplierid=data.username, status="delivering")
    return render(request, 'supplier/supplierpage.html', {'supplier':data,'neworders':neworder,'processing':processing,'delivering':delivering})

def markasbeingprocessed(request,orderid):
    data = order.objects.get(orderid=orderid)
    data.status = "processing"
    data.save()
    create_log("Started Processing",orderid,data.supplierid)
    return redirect(request.META['HTTP_REFERER'])

def markasdispatched(request,orderid):
    data = order.objects.get(orderid=orderid)
    data.status = "delivering"
    data.save()
    create_log("Started Delivering",orderid,data.supplierid)
    return redirect(request.META['HTTP_REFERER'])

def markascompleted(request,orderid):
    data = order.objects.get(orderid=orderid)
    data.status = "completed"
    data.save()
    create_log("Completed Delivery",orderid,data.supplierid)
    return redirect(request.META['HTTP_REFERER'])

def productslist(request,supplierid):
    list = product.objects.filter(supplierid=supplierid)
    return render(request, 'supplier/productslist.html', {'list':list,'supplierid':supplierid})

def productdetail(request,case,supplierid,productid):
    if case == 'del':
        data = product.objects.get(id=productid)
        data.delete()
        return redirect('/details/products/'+str(supplierid))
    elif case == 'edit':
        if request.method == 'GET':
            data = product.objects.get(id=productid)
            data = productform(instance=data)
        elif request.method == 'POST':
            data = productform(request.POST)
            if data.is_valid():
                prod = product.objects.get(id=productid)
                prod.name = data.cleaned_data['name']
                prod.desc = data.cleaned_data['desc']
                prod.price = data.cleaned_data['price']
                prod.availability = data.cleaned_data['availability']
                prod.save()
                return redirect('/details/products/'+str(supplierid))
    elif case == 'add':
        if request.method == 'GET':
            data = productform()
        elif request.method == 'POST':
            data = productform(request.POST)
            if data.is_valid():
                name = data.cleaned_data['name']
                desc = data.cleaned_data['desc']
                price = data.cleaned_data['price']
                avail = data.cleaned_data['availability']
                prod = product(name=name,desc=desc,price=price,availability=avail,supplierid=supplierid)
                prod.save()
                return redirect('/details/products/'+str(supplierid))
    return render(request, 'supplier/productdetail.html', {'pform':data,'supplierid':supplierid,'productid':productid})

def displaylogs(request,supplierid):
    supplier = users.objects.get(id=supplierid).username
    details = log_order.objects.filter(supplierid=supplier).order_by("created")
    return render(request, 'supplier/logs.html', {'logs':details})

def showrevenue(request,supplierid):
    totalrevenue = 0
    print(supplierid)
    try:
        supplier = users.objects.get(id=supplierid).username
    except:
        supplier = ""
    details = order.objects.filter(supplierid=supplier,status="completed")
    for d in details:
        totalrevenue += d.totalprice
    return render(request, 'supplier/revenue.html', {'revenue':details, 'totalrevenue':totalrevenue})

def create_log(case,orderid,supplierid):
    new = log_order(orderid=orderid,supplierid=supplierid,status=case)
    new.save()

def createorder(request,supplierid):
    if request.method == 'GET':
        form = orderform()
    elif request.method == 'POST':
        form = orderform(request.POST)
        if form.is_valid():
            orderid = id_generator()
            buyerid = 1
            suppliername = request.user.username
            productname = form.cleaned_data['productname']
            productid = product.objects.get(name=productname).id
            qty = form.cleaned_data['qty']
            pr = product.objects.get(supplierid=supplierid,id=productid)
            totalprice = pr.price * qty
            status = "neworder"
            new = order(orderid=orderid,productid=productid,buyerid=buyerid,supplierid=suppliername,
                        productname=productname,qty=qty,totalprice=totalprice,status=status)
            new.save()
            return redirect(reverse('supplierpage'))
    return render(request, 'supplier/createorder.html', {'form':form})

def id_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#ERRORS - some function requires "exception", 
#therefore it has to be separated with the one redirected manually
def err_403(request,exception):
    return render(request, 'supplier/error_403_forbidden.html')

def error_403(request):
    return render(request, 'supplier/error_403_forbidden.html')

def err_404(request,exception):
    return render(request, 'supplier/error_404_notfound.html')

def error_404(request):
    return render(request, 'supplier/error_404_notfound.html')

def err_405(request,exception):
    return render(request, 'supplier/error_405_methodnotallowed.html')

def error_405(request):
    return render(request, 'supplier/error_405_methodnotallowed.html')

def err_500(request):
    return render(request, 'supplier/error_500_internalservererror.html')

def error_500(request):
    return render(request, 'supplier/error_500_internalservererror.html')

def feature_coming_soon(request):
    return render(request, 'supplier/notavailable_featurecomingsoon.html')
