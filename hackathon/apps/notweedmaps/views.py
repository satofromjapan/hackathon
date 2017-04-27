# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    if 'id' in request.session:
        return redirect('/show')
    return render(request, 'notweedmaps/index.html')

def show(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'notweedmaps/index.html')
