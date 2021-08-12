from django.shortcuts import render
from django.http import HttpResponse

def display(req):
    return HttpResponse("We are showing polls display view here...")

def place(req, place_id):
    return HttpResponse("Welcome you to %s" %place_id)

def resturant(req):
    return HttpResponse("Welcome you to %s resturant" %resturant)
    
def waiter(req):
    return HttpResponse("Waiter section")