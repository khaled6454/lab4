from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>this is a site to calculate tax<h1>")
def tax(request,price):
        return HttpResponse(f"<h1>Done the number is {price}<h1>")
def taxrate(request,price):
        tax_rate = price * 1.15
        return render(request,"home.html",{"tax_rate":tax_rate})



# Create your views here.
