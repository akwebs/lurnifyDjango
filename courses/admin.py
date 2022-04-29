from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# need to register all models here


class course_datesInline(admin.TabularInline):
    model = course_dates
    extra = 3
    readonly_fields=('created_by','updated_by')

class unitInline(admin.TabularInline):
    model = unit
    extra = 3
    readonly_fields=('created_by','updated_by')

class subTopicInline(admin.TabularInline):
    model = subtopic
    extra = 3
    readonly_fields=('created_by','updated_by')

class topicInline(admin.TabularInline):
    model = topic
    extra = 3
    readonly_fields=('created_by','updated_by')

class subTopicInline(admin.TabularInline):
    model = subtopic
    extra = 3
    readonly_fields=('created_by','updated_by')

class subTopic_textInline(admin.TabularInline):
    model = subbtopic_text
    extra = 3
    readonly_fields=('created_by','updated_by')



@admin.register(course)
class courseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['name','stream_id','description','duration','start_date','end_date','course_expires',]
    list_filter = ['stream_id']
    readonly_fields=('created_by','updated_by')
    search_fields = ['name']
    ordering = ['name']
    inlines = [course_datesInline]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)


@admin.register(course_dates)
class course_datesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','course_id','deadline_date','image')
    readonly_fields=('created_by','updated_by')
    list_filter = ['course_id',]
    def deadline_date(self, obj):
        return obj.course_completion_date.strftime("%d %B %Y | %A")


    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)


@admin.register(stream)
class streamAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['stream_name','created_by','created_at','updated_at']
    readonly_fields=('created_by','updated_by')
    search_fields = ['stream_name']
    ordering = ['stream_name']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)


@admin.register(subjects)
class subjectsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['subject_name','duration']
    search_fields = ['subject_name']
    readonly_fields=('created_by','updated_by')
    ordering = ['subject_name']
    inlines = [unitInline]
    
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)    

@admin.register(unit)
class unitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['subject_id','unit_name','duration']
    search_fields = ['unit_name']
    readonly_fields=('created_by','updated_by')
    ordering = ['unit_name']
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)    
@admin.register(chapter)
class chapterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','subjects_id','unit_id','chapter_name','duration']
    search_fields = ['chapter_name']
    readonly_fields=('created_by','updated_by')
    ordering = ['chapter_name']
    inlines = [topicInline]
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)    
@admin.register(topic)
class topicAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['chapter_id','topic_name','duration']
    search_fields = ['topic_name']
    readonly_fields=('created_by','updated_by')
    ordering = ['topic_name']
    inlines = [subTopicInline]
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)    

@admin.register(subtopic)
class subtopicAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['topic_id','subtopic_name','duration']
    search_fields = ['subtopic_name']
    readonly_fields=('created_by','updated_by')
    ordering = ['subtopic_name']
    inlines = [subTopic_textInline]
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)    
@admin.register(subbtopic_text)
class subbtopic_textAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['subtopic_id','subtopic_text']
    search_fields = ['subtopic_text']
    readonly_fields=('created_by','updated_by')
    ordering = ['subtopic_text']
    def save_model(self, request, obj, form, change):
        if not obj.created_by:  # if obj does not have a creator
            obj.created_by = request.user
        else:
            obj.updated_by = request.user    
        super().save_model(request, obj, form, change)    