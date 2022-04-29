from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *




class UserAccountAdmin(UserAdmin):
    list_display=('phone','username','is_verified')
    search_fields=('phone',)
    readonly_fields=('id',)
    order_by=('username',)
    filter_horizontal=()
    list_filter=('active',)
    fieldsets=(
        ('Personal',
            {
                'fields':('username','phone','otp')
            }),
        (
            'Details',
            {
                'fields':('active','staff','admin')
            }),
            ('Permissions', {'fields': (
            'groups','user_permissions',
            )}),
         
        
    )

admin.site.register(Account,UserAccountAdmin) 

