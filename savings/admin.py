# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import School, Agent, Parent

class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'house_address', 'work_address')

admin.site.register(School)
admin.site.register(Agent)
admin.site.register(Parent, ParentAdmin)