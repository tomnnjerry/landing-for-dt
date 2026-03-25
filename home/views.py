from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html', context)




# --- THE NARRATIVES ---
def about_us(request):
    return render(request, 'pages/about.html')

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