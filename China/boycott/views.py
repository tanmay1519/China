from django.shortcuts import render
from .models import Product
from django.contrib import messages
# Create your views here.
def home (request):
    return render(request,'boycott/Home.html')
def Atma (request):
    return render(request,"boycott/atmanirbhar.html")
def result (request):
    if request.method == "POST":
      product= request.POST.get('content','')
      userCat= request.POST.get('categ','')
      ruthless = product.lower ()
      loweredCat= userCat.lower()
      check=Product.objects.all()
      rendered = []
      categ=[]
      for i in check :
          if ruthless in i.ChinaPr.lower()  and len(product)>0:
              rendered.append(i)
          if loweredCat in i.category.lower() and len (userCat) >0:
              categ.append((i))
      if len(rendered)>0:
        return render(request,"boycott/display.html",{'Product':rendered[0]})
      else :
          if len (categ)>0:
              return render(request, "boycott/display.html", {'Product': categ[0]})
          else :
            messages.warning(request, 'Please Check your Search Query')
            return render(request,"boycott/Home.html")
    return render(request,"boycott/Home.html")

def add (request):
    if request.method=="POST":
        sKey = request.POST.get('sk', '')
        CPR = request.POST.get('cp', '')
        categ = request.POST.get('cat', '')
        ind1 = request.POST.get('ind1', '')
        ind2 = request.POST.get('ind2', '')
        int1 = request.POST.get('int1', '')
        int2 = request.POST.get('int2', '')
        if sKey == 15192309 :
            messages.warning(request, 'You Cannot add a Product')
            return render (request,"boycott/add.html")
        else :
            product = Product (
                ChinaPr=CPR,
                category=categ,
                IndPr1=ind1,IndPr2=ind2, WorPr1=int1,
                WorPr2=int2
            )
            product.save()
            messages.success(request,"Added Successfully")
    return render(request,"boycott/add.html")


