from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
import datetime

def ProductList(request):
    products = Product.objects.all().order_by('Id')
    context = {"products":products}
    return render(request,"Product/index.html",context)

def Add(request):
    if request.method == "POST":
        ProductName = request.POST["ProductName"]
        UnitPrice = request.POST["UnitPrice"]
        Quantity_Abbr = request.POST["QuantityName"]
        CreatedOn = datetime.datetime.now()
        ProductData = Product.objects.create(ProductName=ProductName,UnitPrice=UnitPrice,Quantity_abbr=Quantity_Abbr,CreatedOn=CreatedOn)
        ProductData.save()
        messages.add_message(request, messages.SUCCESS, "Product Added Successfully")
        return redirect('ProductList')
    else:
        return render(request,"Product/Add.html")

def Edit(request, productId):
    if request.method == "POST":
        id = request.POST["Id"]
        ProductName = request.POST["ProductName"]
        UnitPrice = request.POST["UnitPrice"]
        Quantity_Abbr = request.POST["QuantityName"]
        ProductData = Product.objects.get(Id=id)
        ProductData.ProductName = ProductName
        ProductData.UnitPrice = UnitPrice
        ProductData.Quantity_abbr = Quantity_Abbr
        ProductData.UpdatedOn = datetime.datetime.now()
        ProductData.save()
        messages.add_message(request, messages.SUCCESS, "Product Edited Successfully")
        return redirect('ProductList')
    else:
        product = Product.objects.get(Id = productId)
        context = { 'product' : product }
        return render(request, 'Product/Edit.html', context)