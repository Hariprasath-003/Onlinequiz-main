from django.contrib import admin
from .models import Course, Question, Result

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'question_number', 'total_marks')
    search_fields = ('course_name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'question', 'marks', 'answer')
    search_fields = ('question',)
    list_filter = ('course',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks', 'date')
    list_filter = ('exam', 'date')
    search_fields = ('student__name', 'exam__course_name')

