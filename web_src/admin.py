from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    pass

@admin.register(privacy_policy)
class privacy_policyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','heading','description')

@admin.register(hero_section)
class hero_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','description','btn_text','btn_link','image')

@admin.register(feature_section)
class feature_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('s_no','icon','heading','description')

@admin.register(video_section)
class video_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','img_1','img_1_alt','img_2','img_2_alt','img_3','img_3_alt','video_link')


@admin.register(growth_section)
class growth_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading','btn_1_text','btn_1_link','btn_2_text','btn_2_link')

@admin.register(growth_section_data)
class growth_section_dataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading','description', 'icon')

@admin.register(steps_section)
class steps_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'heading',
        'btn_1_text',
        'btn_1_link',
        'btn_2_text',
        'btn_2_link'
    )

@admin.register(steps)
class stepsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('top_heading','heading','image','img_alt')


@admin.register(testimonial_section)
class testimonial_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading', 'no_of_testimonial')

@admin.register(testimonials)
class testimonialsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','testimonial','rank')

@admin.register(faq_section)
class faq_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading','description')
@admin.register(faq)
class faqAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('question','answer')
    
@admin.register(pricing_section)
class pricing_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading','description')

@admin.register(pricing_table)
class pricing_tableAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('course_name','price','btn_text','btn_link')

@admin.register(showcase_section)
class showcase_sectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading', 'description' )

@admin.register(showcase_section_data)
class showcase_section_dataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('heading','description','image','img_alt')

