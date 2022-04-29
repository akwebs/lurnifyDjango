from django.contrib import admin
from admin_section.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(payment_allow_days)
admin.site.register(academic_limits)


@admin.register(cash_coupons)
class cash_couponsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('coupon_name','coupon_value','expires_at',)


@admin.register(monthly_challange_criteria)
class monthly_challange_criteriaAdmin(admin.ModelAdmin):    
    list_display = (
        "test_performance",
        "weekly_challange",
    
    )
    readonly_fields=('created_by','updated_by')


class WeeksInline(admin.StackedInline):
    model = weekly_challange
    extra = 0
    readonly_fields=('created_by','updated_by')

class RewardInline(admin.StackedInline):
    model = weekly_reward
    extra = 0
    readonly_fields=('created_by','updated_by')    


@admin.register(lurnifighter_badges)
class lurnifighter_badgesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('level_name', )
    search_fields = ('level_name',)
    inlines = [WeeksInline]
    readonly_fields=('created_by','updated_by')

@admin.register(weekly_challange)
class weekly_challangeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = (
        'id',
        'lurnifighter_badges_id',
        'week_number',
        'total_study_hours',
        'total_test',
        'total_crowns',
        'refer_freinds',
        'test_performances',
        'study_effectiveness',
    )
    list_filter = ('lurnifighter_badges_id','created_at', 'updated_at')
    inlines = [RewardInline]
    readonly_fields=('created_by','updated_by')    


@admin.register(lurnifighter_referral)
class lurnifighter_referralAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = (
    'badge_name',
    'reffrral_count',
    'description',
    'top',
    )
    readonly_fields=('created_by','updated_by')

admin.site.register(daily_challenge)
admin.site.register(test_and_study)
  