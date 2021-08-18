from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, I am index.")


def question(request,question_id):
    return HttpResponse("This is question no %s" %question_id)
    

def votes(request,question_id):
    return HttpResponse("Votes for %s question is %s." %( question_id, "votes"))


def result(request,question_id):

    return HttpResponse("result for %s question is %s" %(question_id,"result"))



