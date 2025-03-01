from django.contrib import admin
from .models import Survey, Question, Response

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    inlines = [QuestionInline]

admin.site.register(Question)
admin.site.register(Response)
