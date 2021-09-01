from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, request, response, Http404
from django.http import HttpResponseRedirect
from .models import Document
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, DocumentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from django.utils import timezone
import datetime
from datetime import timedelta


def home(req):
    context = {'files': Document.objects.all()}
    return render(req, 'doc_manage/home.html', context)


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
    return render(req, 'doc_manage/registration.html', {'form': fm})


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
                return redirect('display')
        return render(req, 'doc_manage/login.html')
    else:
        return redirect('display')

@login_required
def welcome_page(req):
    # form = DocumentForm()
    name = req.user.username
    print(name)
    return render(req, 'doc_manage/welcome_page.html', {'context':name })


def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/login/')


# @login_required
def upload_file(req):
    # breakpoint()
    if req.method == 'POST':
        form = DocumentForm(req.POST, req.FILES)
        # breakpoint()
        if req.user.is_authenticated:
            user=(req.user.id)
            user_obj=User.objects.get(pk=user)
            pdf_per_day_limit=Document.objects.filter(user=user_obj.pk).filter(created_at__date=timezone.now()).count()

            # breakpoint()
            if pdf_per_day_limit==5:
                # breakpoint()
                messages.info(req,"you have reached the daily limit wait unitill 12 pm to upload more")
                return redirect('upload')
            else:
                # breakpoint()
                if form.is_valid():
                    document = Document.objects.create(
                        user=user_obj,
                        title=form.cleaned_data['title'],
                        data = form.cleaned_data['data']
                    )
                    document.save()
                    messages.success(req, "Document created successfully")
                    return HttpResponseRedirect('/upload/')
                else:
                    messages.error(req, form.errors['data'])
                    return redirect('upload')
        return redirect('login')
    else:
        form = DocumentForm()
        return render(req, 'doc_manage/upload.html', {'context': form})


# @login_required
def download(req, path):
    if req.user.is_authenticated:
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path,'rb') as f:
                response=HttpResponse(f.read(), content_type="application/data")
                response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
                return response
        raise Http404
    return redirect('login')


def display_data(req):
    if req.user.is_authenticated:
        today = datetime.date.today()
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        user=req.user.username

        if req.method == 'GET':
            report_type = req.GET.get('report_type')
            if report_type == 'sort_by_name':
                user_data = Document.objects.filter(user=User.objects.get(username=req.user.username)).order_by('title')
                return render(req, 'doc_manage/display.html', {'context': user_data,'user':user.upper()})

            elif report_type == 'current_month':
                '''filter with month value'''

                user_data = Document.objects.filter(user=User.objects.get(username=user)).filter(created_at__month = current_month)
                return render(req, 'doc_manage/display.html', {'context': user_data})


            elif report_type == 'current_month':
                '''filter with year value'''
                # pdf_list = user_docs.filter(created_at__month=request.GET['month'])

                user_data = Document.objects.filter(user=User.objects.get(username=user)).filter(created_at__year = current_year)
                return render(req, 'doc_manage/display.html', {'context': user_data})


            elif report_type == 'within':
                '''filter with start date and end date'''
                # pdf_list = user_docs.filter(created_at__month=request.GET['month'])
                print("\n\n within range date metho")
                print(report_type)
                print
                user_data = Document.objects.filter(user=User.objects.get(username=user).filter(created_at__year = current_year))
                return render(req, 'doc_manage/display.html', {'context': user_data})

            else:
                user_data = Document.objects.filter(user=User.objects.get(username=req.user.username)).order_by('id')
                return render(req, 'doc_manage/display.html', {'context': user_data})

        elif req.method=='POST':
            # breakpoint()
            start_date = req.POST['startdate']
            print(start_date)
            end_date = req.POST['enddate']
            user_data = Document.objects.filter(user=req.user, created_at__range=[start_date,end_date])

            return render(req, 'doc_manage/display.html', {'context': user_data})

    return redirect('login')




