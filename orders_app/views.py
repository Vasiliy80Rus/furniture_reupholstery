from django.shortcuts import render
from django.http import  HttpRequest, HttpResponse


def view_orders(request: HttpRequest) -> HttpResponse:
    return render(request, 'fabrics/index.html')
    
