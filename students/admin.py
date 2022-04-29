from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(student_profile)
class student_profileAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'email', 'phone', 'address', 'city', 'state', 'pin_code', 'country', 'date_of_birth', 'created_at', 'updated_at')
    search_fields = ('student_name',)




@admin.register(academic_details)
class academic_detailsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'stream_id', 'course_id', 'course_start_date', 'course_completion_date', 'target_rank', 'daily_pace', 'academic_limits_id' ,'created_at', 'updated_at')
    list_filters = ('student_id', 'stream_id', 'course_id', 'course_completion_date',  'created_at', 'updated_at') 
    search_fields = ('student_id',)

@admin.register(students_referral)
class students_referralAdmin(admin.ModelAdmin):
    list_display = ('referral_sent_student', 'referral_get_student')
    list_filters = ('referral_sent_student', ) 
    search_fields = ('referral_sent_student',)




@admin.register(lurnifighter_levels)
class lurnifighter_levelsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = (
        'student_id',
        'weekly_challange_id',
        'level_status',
    )
    list_filters = ('student_profile_id', 'weekly_challange_id', 'level_start_date', 'level_end_date',)


@admin.register(lurnifighter_coupons)
class lurnifighter_couponsAdmin(admin.ModelAdmin):
    list_display=(
            "student_id",
            "weekly_challange_id",
            "weekly_reward_id",
            "referral_coupon",
    )
    list_filters = ('student_profile_id', 'lurnifighter_badges_id',)


@admin.register(lurnifighter_badges_status)
class lurnifighter_badges_statusAdmin(admin.ModelAdmin):
    list_display = (
       'student_id',
        'lurnifighter_badges_id',
        'is_completed',
        'created_at',
        'updated_at',
    )


@admin.register(lurnifighter_cashcoupons)
class lurnifighter_cashcouponsAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "got_for",
        "cash_coupons_id",
        "is_used",
        "expires_at",
    )

    def expires_at(self, obj):
        return obj.cash_coupons_id.expires_at
    



@admin.register(monthly_certificate)
class monthly_certificateAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "monthly_challange_criteria_id",
        "test_performance",
        "weekly_challange",
        "month_name",
        "certificate",
    )



    
admin.site.register(lurnifighter_daily_challenge)      

class installment_inline(admin.StackedInline):
    model = payment_installments
    extra = 0
    

@admin.register(student_payments)
class student_paymentsAdmin(admin.ModelAdmin):
    list_display=(
        "student_id",
        "allow_days",
        "allow_date",
        "course_id",
        "course_dates_id",
        "total_amount",
        "remain_amount",
        "paid_amount",
        "total_paid",
    )
    inlines = [installment_inline]

    
@admin.register(payment_installments)
class payment_installmentsAdmin(admin.ModelAdmin):
    list_display = (
        "student_payments_id",
        "installment_no",
        "installment_amount",
    )


@admin.register(student_study)
class student_studyAdmin(admin.ModelAdmin):
    list_display = (
        "studentId",
        "courseId",
        "subjectId",
        "unitId",
        "chapterId",
        "chapterDuration",
        "newChapterDuration",
        "topicId",
        "topicDuration",
        "newTopicDuration",
        "startDatetime",
        "endDatetime",
        "startDate",
        "studiedTime",
        "studyStatus",
        "coins",
        "eNess",
        "totalDuration",
    )
