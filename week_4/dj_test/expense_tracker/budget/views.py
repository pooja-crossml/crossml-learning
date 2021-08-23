from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime
from budget.models import Expenses, Budget

def index(req):
    expenses = Expenses.objects.all()
    return render(req, 'budget/index.html', {'context':expenses})

def display(req, id):
    expense = Expenses.objects.get(pk=id)

    # now = timezone.now()
    # print("current: "+ str(now.month))
    # one_month_ago = datetime.datetime(now.year, now.month - 1, 1)
    # print("previous "+str(one_month_ago.month))
    # month_end = datetime.datetime(now.year, now.month, 1) - datetime.timedelta(seconds=1)
    # print("current_year"+str(month_end.year))
    
    return render(req, 'budget/detail.html', {'context':expense})
    

def expense(req,id):
    
    now = timezone.now().month
    return render(req, 'budget/expense.html', {'context': now})




