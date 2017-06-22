# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class Task(models.Model):
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=200)
	explanation = RichTextField()

	def __str__(self):
		return self.question
