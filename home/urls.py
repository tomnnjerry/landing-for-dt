
from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    # Core Narratives
    path('about-us/', views.about_us, name='about_us'),
    path('the-team/', views.team_list, name='team_list'),
    path('the-team/<slug:member_slug>/', views.team_detail, name='team_detail'),
    
    # The Expeditions (Itineraries)
    path('itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itineraries/nepal-tour/', views.nepal_tour, name='nepal_tour'),
    path('itineraries/darjeeling-tour/', views.darjeeling_tour, name='darjeeling_tour'),
    
    # Interactions
    path('gallery/', views.gallery, name='gallery'),
    path('contact-host/', views.contact_host, name='contact_host'),
    path('book-appointment/', views.booking_appointment, name='booking_appointment'),
    path('partner-with-us/', views.partner_with_us, name='partner_with_us'),
    
    # The Sovereign Legalities
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
] 