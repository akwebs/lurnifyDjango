from django.contrib import admin
from .models import *
from django.utils.html import format_html



@admin.register(member_type)
class lurnify_membersAdmin(admin.ModelAdmin):
    list_display = (    
                    'id',
                    'type_name',
                    )

@admin.register(lurnify_member)
class lurnify_membersAdmin(admin.ModelAdmin):
    list_display=('id','account_id','phone','name','member_type','address','created_at','updated_at')                  
    list_filter = ('member_type',)


@admin.register(Bank_detail)
class lurnify_BankAdmin(admin.ModelAdmin):
    list_display=('id','lurnify_member_id','bank_name','branch_name','ifsc_code','account_no','created_at','updated_at')                  
    list_filter = ('lurnify_member_id',)

@admin.register(referal_code)
class lurnify_referalAdmin(admin.ModelAdmin):
    list_display=('id','lurnify_member_id','qr_code_number','qr_code','created_at','updated_at')                  
    list_filter = ('lurnify_member_id',)

    