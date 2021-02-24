# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.views import generic
from django.template.context_processors import csrf

from .models import Student
# Create your views here.


def getstudentinfo(request):
    c={}
    c.update(csrf(request))
    return render_to_response('addstudentinfo.html',c)

def addstudentinfo(request):
    if request.method == 'POST':
        sname = request.POST.get('studentname','')
        sdate = request.POST.get('birthdate','')
        s = Student(student_name = sname,student_dob=sdate)
        s.save()
        return HttpResponseRedirect('/firstdbtest/addsuccess/')
    else:
        return HttpResponse("invalid")
    

def addsuccess(request):
    return render_to_response('addrecord.html')

class StudentListView(generic.ListView):
    model = Student

