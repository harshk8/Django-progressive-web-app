from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from . models import feed, Traffic
import json
import datetime
import requests

# Create your views here.
def index(request):
    template='posts/index.html'
    results = feed.objects.all()
    traffic = Traffic.objects.all().order_by('-id')
    jsondata = serializers.serialize('json', results)

    context={
        'traffic':traffic,
        'results':results,
        'jsondata':jsondata,
    }
    return render(request,template,context)

def getdata(request):
    results=feed.objects.all()
    jsondata = serializers.serialize('json',results)
    return HttpResponse(jsondata)

def base_layout(request):
    template='posts/base.html'
    return render(request,template)


def note_traffic(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')

    get_ip= Traffic() #imported class from model
    get_ip.ip= ipaddress
    get_ip.created_at = datetime.datetime.now() #import datetime
    get_ip.save()

    data = requests.get('https://ipinfo.io/{}'.format(ipaddress))
    if data.status_code == 200:
        json_data = json.loads(data.content)

        get_ip.country = json_data['country']
        get_ip.city = json_data['city']
        get_ip.timezone = json_data['timezone']
        get_ip.region = json_data['region']
        get_ip.save()

    return redirect('/index')