from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Building)
admin.site.register(Tenant)
admin.site.register(BuildingTenant)
admin.site.register(Tag)
