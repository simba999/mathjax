# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *


def index(request):
	form = TaskAdminForm()
	return render(request, 'index-jax.html', locals())

	
def index_(request):
	return render(request, 'index.html')
