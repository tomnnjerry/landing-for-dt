from django.contrib import admin
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'inquiry_type', 'status', 'created_at')
    list_filter = ('inquiry_type', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone_number')
        }),
        ('Inquiry Details', {
            'fields': ('description', 'inquiry_type')
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def __str__(self):
        return 'Contact Inquiry'
