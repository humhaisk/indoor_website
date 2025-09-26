# Admin : 'SK' and Pasword : 'SK@12345'
from django.contrib import admin
from mic_general.models import Organizing_Committee

# Register your models here.
class Organizing_CommitteeAdmin(admin.ModelAdmin):
    list_display = ('unique_id','member_Name','member_Role','member_Department','member_YOG','member_InstaID', 'member_Pic')   

admin.site.register(Organizing_Committee, Organizing_CommitteeAdmin)
