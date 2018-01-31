# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)

def mark_on_the_map(request):
    template_name = 'home.html'
    context = {}
    if request.body and 'location' in request.body:
        locations = request.body['location']
        context['location'] = locations
    return render(request, template_name, context)