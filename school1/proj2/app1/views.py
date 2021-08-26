from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Numofstudents, Attendence
from datetime import datetime
from django.conf import settings
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


# Create your views here.

def listofstu(request):
    data = Numofstudents.objects.all()
    request.session['date'] = datetime.now().strftime('%d/%m/%Y')
    request.COOKIES['ip'] = IPAddr
    return render(request, "base.html", {"data": data, 'date': request.session['date'], 'ip': request.COOKIES['ip']})


def present(request, pk):
    data = Numofstudents.objects.get(pk=pk)
    test = datetime.now()
    if not Attendence.objects.filter(Name=data.Name).filter(datefield=test.strftime('%Y-%m-%d')):
        attend = Attendence(Name=data.Name, datefield=test.strftime('%Y-%m-%d'), status='present')
        attend.save()
        return HttpResponse('Data stored successful')
    return HttpResponse('Attendance already captured')


def absent(request, pk):
    data = Numofstudents.objects.get(pk=pk)
    test = datetime.now()
    if not Attendence.objects.filter(Name=data.Name).filter(datefield=test.strftime('%Y-%m-%d')):
        attend = Attendence(Name=data.Name, datefield=test.strftime('%Y-%m-%d'), status='absent')
        attend.save()
        send_mail(
            f"child attendance status",
            f"your child {data.Name} is absent today please confirm with us",
            settings.EMAIL_HOST_USER,
            [  ]
        )
        return HttpResponse('Attendance captured for the day')
    return HttpResponse('Attendance already captured')
