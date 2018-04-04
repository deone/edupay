# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import School, Agent, Parent, SavingPlan, Saving

class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'house_address', 'work_address')

class SavingPlanAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'amount_to_be_saved', 'target_date', 'contribution')

    def parent_name(self, obj):
        return obj.parent.get_full_name()

admin.site.register(School)
admin.site.register(Agent)
admin.site.register(SavingPlan, SavingPlanAdmin)
admin.site.register(Saving)
admin.site.register(Parent, ParentAdmin)