from django import forms
from .models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):
    """Form for contact inquiries from popup modal"""
    
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Phone Number',
            'type': 'tel',
        })
    )
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Full Name',
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address',
            'type': 'email',
        })
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Tell us about your trip, budget, dates, or any special requests...',
            'rows': 5,
        })
    )
    
    class Meta:
        model = ContactInquiry
        fields = ['name', 'phone_number', 'email', 'description', 'inquiry_type']
        widgets = {
            'inquiry_type': forms.HiddenInput(),
        }
