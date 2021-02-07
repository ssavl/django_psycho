from django.contrib import admin
from .models import PsychoMaster, Method, RawData, RawMethod


admin.site.register(PsychoMaster)
admin.site.register(Method)
admin.site.register(RawData)
admin.site.register(RawMethod)

