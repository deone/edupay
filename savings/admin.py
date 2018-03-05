# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import School, Agent

admin.site.register(School)
admin.site.register(Agent)