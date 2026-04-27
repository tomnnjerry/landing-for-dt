from django.db import models

class ContactInquiry(models.Model):
    """Store all customer inquiries from popup forms"""
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    # Allow any inquiry type (buttons, locations, custom)
    inquiry_type = models.CharField(max_length=100, default='general')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'
    
    def __str__(self):
        return f"{self.name} - {self.inquiry_type} ({self.created_at.strftime('%Y-%m-%d')})"
