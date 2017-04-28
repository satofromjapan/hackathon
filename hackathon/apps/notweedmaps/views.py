# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from urllib2 import urlopen, URLError, Request
import json

def index(request):
    # if 'id' in request.session:
    #     return redirect('/show')
    return render(request, 'notweedmaps/index.html')

def process(request):
    #birthday validation logic
    birthday = request.POST['birthday']
    bday = datetime.strptime(birthday, '%m/%d/%Y').date()
    today = datetime.today().date()
    print "bday:", bday.year
    print "today:", today.year
    age = (today.year - bday.year)
    print "age:", age
    if age < 21:
        messages.error(request, 'You must be 21 or older to use this site!')
        return redirect('/')
    else:
        return redirect('/show')

def show(request):
    # if 'id' not in request.session:
    #     return redirect('/')
    # url = "https://data.sfgov.org/api/views/8r8e-q58k/rows.json"
    # response = urlopen(url)
    # data=json.loads(response.read())
    # # print data['data'][0][8]
    # arr = []
    #
    # for i in data['data']:
    #     str = i[9]
    #     str = str[7:-1]
    #     str = str.split(" ")
    #     arr.append({
    #     "bussiness_name": i[8],
    #     "address": i[11] + " " + i[12] + " " +  i[13] + " " + i[14],
    #     "location_type": i[18],
    #     "neighborhood": i[19],
    #     "id": i[24],
    #     "zipcode": i[14],
    #     "lat": str[1], "lng": str[0]})
    #
    # context = {
    # "arr": arr,
    # }
    return render(request, 'notweedmaps/weed2.html')
