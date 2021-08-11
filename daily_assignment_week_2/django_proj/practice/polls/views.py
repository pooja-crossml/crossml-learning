from django.shortcuts import render
from django.http import HttpResponse

def display(req):
    return HttpResponse("We are showing polls display view here...")