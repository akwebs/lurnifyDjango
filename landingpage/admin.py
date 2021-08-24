from django.contrib import admin

from .models import Register, Question

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'dream', 'email', 'mobile', 'createdAt')

admin.site.register(Register, RegisterAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','qid','que','option1','option2','option3','option4')

admin.site.register(Question, QuestionAdmin)
