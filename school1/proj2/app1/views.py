from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Numofstudents,Attendence
from datetime import datetime
# Create your views here.

def listofstu(request):
    data = Numofstudents.objects.all()
    request.session['date'] = datetime.now().strftime('%d/%m/%Y')
    return render(request,"base.html",{"data":data, 'date':request.session['date']})
def present(request,pk):
    data = Numofstudents.objects.get(pk=pk)
    test = datetime.now()
    if not Attendence.objects.filter(Name=data.Name).filter(datefield=test.strftime('%Y-%m-%d')):
        attend = Attendence(Name=data.Name,datefield=test.strftime('%Y-%m-%d'),status='present')
        attend.save()
        return HttpResponse('Data stored successful')
    return HttpResponseRedirect('/')

def absent(request,pk):
    data = Numofstudents.objects.get(pk=pk)
    test = datetime.now()
    if not Attendence.objects.filter(Name=data.Name).filter(datefield=test.strftime('%Y-%m-%d')):
        attend = Attendence(Name=data.Name,datefield=test.strftime('%Y-%m-%d'),status='absent')
        attend.save()
        return HttpResponse('Data stored successful')
    return HttpResponseRedirect('/')



