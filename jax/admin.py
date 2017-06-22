# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from jax.forms import *

class TaskAdmin(admin.ModelAdmin):
	form = TaskAdminForm

admin.site.register(Task, TaskAdmin)
