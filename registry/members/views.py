# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render
from django.template.context_processors import  csrf
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
from django.db import transaction

from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import  auth
from .models import Profile
#from .forms import UserForm,ProfileForm,paynumberform
from django.db import transaction
from django.contrib.messages import constants as messages
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from models import*
from forms import*

import djqscsv
import csv
#from forms import ContactForm
#upload file

#end upload file
def index(request):
    return render(request,'index.html')


def login_user(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        to_emails=request.user.email
        ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ip:
            ip = ip.split(", ")[0]
        else:
            ip = request.META.get("REMOTE_ADDR", "")
        send_mail("Portoriki Church Registry System Security Info","Your Registry System Profile have been access from the IP:"+ str(ip) + ". "+" Please report this to the administraor if you find this suspicious.",
        "Portoriki Church Registry System Security Info <potorikisdasystem@psdachurch.com>", [to_emails])
        return HttpResponseRedirect('/loggin/')

    else:
        return HttpResponseRedirect('/invalid/')

def invalid(request):
    return render_to_response('invalid.html')

@login_required()#only logged in users should access this
def loggin(request):
    username=None
    if request.user.is_authenticated:
        profile_info=request.user.profile
        info=request.user
        return render(request,'dashboard.html',locals(),{'full_name': request.user.first_name})

#log user out
def logout(request):
	auth.logout(request)
	return render(request,'index.html')




@login_required()#only logged in users should access this
@transaction.atomic
def addcontact(request):
    if request.method=='POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            return render(request,'update_successful.html',locals())
            #return HttpResponse('You have Successfuly added a contact')
    else:
        form =ContactForm()
        args={}
        args.update(csrf(request))
        args['form']=form
    return render(request,'new_member.html',args)


def reportboard(request):
    query_name=contacts.objects.all()
    return render(request,'reportdashboard.html',locals())

#church minutes
def manage_minute(request):
    query_name=minutes.objects.all()
    return render(request,'minutesboard.html',locals())

#adding new minutes
@login_required()#only logged in users should access this
@transaction.atomic
def addminute(request):
    if request.method=='POST':
        form =addminuteform(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            return render(request,'update_successful.html',locals())
            #return HttpResponse('You have Successfuly added a contact')
    else:
        form =addminuteform()
        args={}
        args.update(csrf(request))
        args['form']=form
    return render(request,'new_minute.html',args)


#update minute
@login_required()#only logged in users should access this)
@transaction.atomic
def updateminute(request,id):
    if request.method=='POST':
        minute=minutes.objects.get(id=id)
        form=addminuteform(request.POST, instance=minute)
        if form.is_valid():
            form.save()
            return render_to_response('update_successful.html')

    else:
        minute=minutes.objects.get(id=id)
        form=addminuteform(instance=minute)
    return render(request,'update_minute.html',{'form':form})

#drop minutes

@login_required()#only logged in users should access this
@transaction.atomic
def drop_minute(request,id):
    if request.method == 'POST':
        drop=minutes.objects.get(id=id)
        form =addminuteform(request.POST, instance=drop)
        if form.is_valid():
            drop.delete()
            return render_to_response('delete_successful.html')
    else:
        drop=minutes.objects.get(id=id)
        form =addminuteform(instance=drop)
    return render(request,'drop.html', {'form': form})

def bydate(request):
    return render(request,'selectdate.html')

#query minute by date
def bydatequery(request):
    if "selectdate" in request.POST:
        selected_minute = request.POST["selectdate"]
        if selected_minute==selected_minute:
            query_name=minutes.objects.filter(date=selected_minute)
            return render(request,'minutesboard.html',locals())



def display_data(request,id):
    selected_objects = minutes.objects.filter(pk__in=id)
    return render(request,'minuterpt.html',locals())




def province(request):
    return render(request,'provinceselec.html')

#query province
def provincequery(request):
    if "sel_province" in request.POST:
        selected_province = request.POST["sel_province"]
        if selected_province==selected_province:
            query_province=contacts.objects.filter(Province=selected_province)
            return render(request,'provincequery.html',locals())



def island(request):
    return render(request,'islandselect.html')


#query island
def islandquery(request):
    if "sel_island" in request.POST:
        selected_island = request.POST["sel_island"]
        if selected_island==selected_island:
            query_island=contacts.objects.filter(Island=selected_island)
            return render(request,'islandquery.html',locals())


def download_registry(request):
	csv_export=contacts.objects.values('First_Name','Middle_Name','Last_Name','Date_of_Birth','Gender','Island','Date_of_Baptism','Province','Congregation','Status','Comments')
	return djqscsv.render_to_csv_response(csv_export)



@login_required()#only logged in users should access this
@transaction.atomic
def edit_user(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method=='POST':

        user_form = ContactForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'success.html')
    #    client_address = request.META['HTTP_X_FORWARDED_FOR']     return redirect('settings:profile')
        else:
            message.error(request, _('Please correct the error and try again'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


    #upload files
def uploadfunc(request):
    if request.method=='POST':
        form =uploadfileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('upload_successful.html')
    else:
        form=uploadfileform()
    return render(request, 'upload.html',{'form':form})





#write to database
#import leave_balance from CSV file
def writeto_db(request):
    with open('/var/www/vmachines/registry/files/members.csv', 'rb') as csvfile:
        readata=csv.reader(csvfile,delimiter=str(','),quotechar=str('"'))
        for row in readata:
            if row[0]!='First_Name':
                data=contacts()
                data.First_Name=row[0]
                data.Middle_Name=row[1]
                data.Last_Name=row[2]
                data.Date_of_Birth=row[3]
                data.Gender=row[4]
                data.Island=row[5]
                data.Province=row[6]
                data.Date_of_Baptism=row[7]
                data.Congregation=row[8]
                data.Status=row[9]
                data.Comments=row[10]
                data.save()
        return render_to_response('writesucc.html',locals())



@login_required()#only logged in users should access this)
@transaction.atomic
def updatecontact(request,id):
    if request.method=='POST':
        contact=contacts.objects.get(id=id)
        form=ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return render_to_response('update_successful.html')

    else:
        contact=contacts.objects.get(id=id)
        form=ContactForm(instance=contact)
    return render(request,'update_member.html',{'form':form})


@login_required()#only logged in users should access this
@transaction.atomic
def kill_entry(request,id):
    if request.method == 'POST':
        kill=contacts.objects.get(id=id)
        form =ContactForm(request.POST, instance=kill)
        if form.is_valid():
            kill.delete()
            return render_to_response('delete_successful.html')
    else:
        kill=contacts.objects.get(id=id)
        form =ContactForm(instance=kill)
    return render(request,'kill.html', {'form': form})
