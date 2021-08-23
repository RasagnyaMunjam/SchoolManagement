from django.contrib import admin
from .models import Attendence,Numofstudents
# Register your models here.
@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['Name','datefield','status']

admin.site.register(Numofstudents)

