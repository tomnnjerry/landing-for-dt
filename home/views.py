from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
import json
from .models import ContactInquiry
from .forms import ContactInquiryForm

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html', context)




# --- THE NARRATIVES ---
def about_us(request):
    return render(request, 'about.html')

def team_list(request):
    # Fetch all team members from your database/context
    return render(request, 'team/list.html')

def team_detail(request, member_slug):
    # Surgical fetch for specific member soul/bio
    # member = get_object_or_404(TeamMember, slug=member_slug)
    return render(request, 'team/detail.html')

# --- THE EXPEDITIONS ---
def itinerary_list(request):
    return render(request, 'itineraries/list.html')

def nepal_tour(request):
    return render(request, 'itineraries/nepal.html')

def darjeeling_tour(request):
    return render(request, 'itineraries/darjeeling.html')

# --- THE GALLERY ---
def gallery(request):
    return render(request, 'pages/gallery.html')

# --- INTERACTIONS (With Data Handling) ---
def contact_host(request):
    if request.method == "POST":
        # Logic to save the 'Dossier' request or Contact form
        messages.success(request, "Your message has reached the Command Center.")
        return redirect('contact_host')
    return render(request, 'pages/contact.html')

def booking_appointment(request):
    if request.method == "POST":
        # Logic for scheduling a host consultation
        return redirect('itinerary_list')
    return render(request, 'pages/booking.html')

def partner_with_us(request):
    return render(request, 'pages/partner.html')

# --- THE LEGALITIES ---
def privacy_policy(request):
    return render(request, 'legal/privacy.html')

def terms_conditions(request):
    return render(request, 'legal/terms.html')

def refund_policy(request):
    return render(request, 'legal/refund.html')

# --- POPUP FORM SUBMISSION ---
@require_http_methods(["POST"])
def submit_inquiry(request):
    """
    Handle AJAX form submission from popup modal.
    Saves inquiry to database and returns JSON response.
    """
    try:
        # Parse JSON data from AJAX request
        data = json.loads(request.body)
        
        # Validate required fields
        required_fields = ['name', 'phone_number', 'email', 'description', 'inquiry_type']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'message': f'{field.replace("_", " ").title()} is required'
                }, status=400)
        
        # Create and save inquiry
        inquiry = ContactInquiry(
            name=data['name'].strip(),
            phone_number=data['phone_number'].strip(),
            email=data['email'].strip(),
            description=data['description'].strip(),
            inquiry_type=data.get('inquiry_type', 'general')
        )
        
        # Validate the model using full_clean (validates all fields including email format)
        try:
            inquiry.full_clean()
        except ValidationError as e:
            # Extract the first error message from validation errors
            error_messages = []
            if hasattr(e, 'error_dict'):
                for field, errors in e.error_dict.items():
                    if errors:
                        error_messages.append(errors[0].message)
            
            error_msg = error_messages[0] if error_messages else 'Please check your input and try again'
            
            return JsonResponse({
                'success': False,
                'message': error_msg
            }, status=400)
        
        inquiry.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you! Your inquiry has been received. Our team will contact you within 24 hours.',
            'inquiry_id': inquiry.id
        })
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }, status=500)