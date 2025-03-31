from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'mobile', 'salary', 'status', 'profile_pic_display')
    search_fields = ('user__first_name', 'user__last_name', 'mobile')
    list_filter = ('status',)

    def profile_pic_display(self, obj):
        if obj.profile_pic:
            return obj.profile_pic.url
        return "No Image"
    profile_pic_display.short_description = "Profile Picture"
