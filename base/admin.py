from django.contrib import admin
from base.models import Products,Addcard,Buy
# Register your models here.
class display(admin.ModelAdmin):
    list_display=['id','name','cost','img','desc']
    ordering=['id']
    list_display_links=['name']
admin.site.register(Products,display)
admin.site.register(Addcard,display)
admin.site.register(Buy,display)