from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'mobile', 'profile_pic_display')
    search_fields = ('user__first_name', 'user__last_name', 'mobile')
    
    def profile_pic_display(self, obj):
        if obj.profile_pic:
            return obj.profile_pic.url
        return "No Image"
    profile_pic_display.short_description = "Profile Picture"

