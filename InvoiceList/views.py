from django.shortcuts import render
from Order.models import Order

# Create your views here.
def InvoiceList(request):
    OrderList = Order.objects.all()
    Context = {"OrderList":OrderList}
    return render(request, "InvoiceList/invoiceList.html",Context)
