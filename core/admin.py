from django.contrib import admin
from .models import StudentResult, Testimonial, ContactSubmission

@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['name', 'board', 'score', 'year', 'is_topper', 'rank']
    list_filter = ['board', 'year', 'is_topper']
    search_fields = ['name']
    list_editable = ['is_topper', 'rank']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'board', 'year', 'score', 'is_featured']
    list_filter = ['board', 'year', 'is_featured']
    list_editable = ['is_featured']

@admin.register(ContactSubmission)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'submitted_at', 'is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'phone', 'email', 'message', 'submitted_at']
    list_editable = ['is_read']
