from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class instructionsInline(admin.TabularInline):
    model = instructions
    extra = 1
    readonly_fields=('created_by','updated_by')


@admin.register(create_test)
class create_testAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('test_name','test_type','test_duration','question_positive_marks','question_negative_marks')
    readonly_fields=('created_by','updated_by','created_at','updated_at')
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)
    inlines= [instructionsInline]    

@admin.register(instructions)
class instructionsAdmin(ImportExportModelAdmin , admin.ModelAdmin):
    list_display = ('create_test','instruction_text')
    readonly_fields=('created_by','updated_by')
    
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(questions_bank)
class questions_bankAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('create_test',
                    'question_text',
                    'question_difficulty',
                    'question_style',
                    'questions_options',
                    'correct_option'
                    
                    )
    readonly_fields=('created_by','updated_by')                
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)                                   
