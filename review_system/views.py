# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import user_review
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

def form_view(request):
    template_name = 'forms.html'
    if request.method == "POST":
        form = user_review(request.POST)
        if form.is_valid():
            post = form.save()
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
    else:
        form = user_review()
    return render(request, template_name, {'form': form})