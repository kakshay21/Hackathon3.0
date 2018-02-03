# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def user_inputs(request):
    template_name = 'user_inputs.html'
    context = {}
    return render(request, template_name, context)
