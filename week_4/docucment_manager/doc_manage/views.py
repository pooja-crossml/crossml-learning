from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse, request, response, Http404
from django.http import HttpResponseRedirect
from .models import Document
from django.contrib.auth import authenticate, login,logout
from .forms import SignUpForm, DocumentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from django.utils import timezone


def home(req):
    context = {'files': Document.objects.all()}
    return render(req, 'doc_manage/home.html', context)

# TODO permission to a user staff true
def sign_up(req):
    if req.method == "POST":
        fm = SignUpForm(req.POST)
        # breakpoint()
        if fm.is_valid():
            # breakpoint()
            fm.is_staff = True
            messages.success(req, 'Account created successfully')            
            fm.save()
            return redirect('login')
    else:
        fm = SignUpForm()
    return render(req, 'doc_manage/registration.html', {'form':fm})


def login_user(req): 
    if not req.user.is_authenticated:
        if req.method == "POST":
            username = req.POST['username']
            password = req.POST['password']
            user = authenticate(req, username=username, password=password)
            # breakpoint()
            if user is not None:
                # return redirect('welcome_page.html')
                login(req, user)
                return HttpResponseRedirect('/welcome/')
        return render(req, 'doc_manage/login.html')
    else:
        return HttpResponseRedirect('/welcome/')    

def welcome_page(req):
    if req.user.is_authenticated:
        return render(req, 'doc_manage/welcome_page.html',{'name': req.user})
    else:
        return HttpResponseRedirect('/login/')



def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/login/')


# @login_required
def upload_file(req):
    pass
    # if  req.method == 'POST':
    # form = DocumentForm(req.POST,req.FILES)
    # user = req.user.username
    # user_obj = User.objects.get(username=user)
    # todays_pdfs = Document.objects.filter(user=user_obj.pk).filter(created_at__date=timezone.now())
    # users_today_uploads = todays_pdfs.count()

    # form = DocumentForm()



# @login_required
def download(req,path):
    pass
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path,'rb') as f:
#             response=HttpResponse(f.read(), content_type="application/data")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response
#     raise Http404


def report_data(req):
    if request.GET:
        report_type = request.GET['report_type']
        if report_type == 'sort_by_name':
            data = Document.objects.all().order_by('title')


    else:
        data = Document.objects.all()
        return render(req, 'doc_manege/report.html', {'context': data})


def report(request):
    if request.GET:
        report_type = request.GET['report_type']
        if report_type == 'current_month':
            data = Expense.objects.filter(created_at__month=today.month)
        elif report_type == 'previous_month':
            data = Expense.objects.filter(created_at__month=previous_month.month)
        elif report_type == 'current_year':
            data = Expense.objects.filter(created_at__year=today.year)
        else:
            data = Expense.objects.all()
    else:
        data = Expense.objects.all()
    return render(request, 'tracker/report.html', {'ExpenseData': data})
