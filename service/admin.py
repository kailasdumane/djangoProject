from django.contrib import admin

#Registering models here.
from django.contrib.admin.sites import site
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

admin.site.register(Service, ServiceAdmin)


