from django.shortcuts import render
from geopy.geocoders import Nominatim
from django.shortcuts import render, redirect
from .models import Donor
import requests
import socket
def index(request):
    return render(request, 'landing-page.html')

def donate(request):
    return render(request, 'index.html')

def patient(request):
    return render(request, 'donate.html')

def success_page_view(request):
    return render(request, 'alert.html')


def search(request):
    if request.method == 'POST':
        location = request.POST.get('location')
    
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(location)
    latitude = getLoc.latitude
    longitude = getLoc.longitude

    api_key = "yaGfFZSYuEPwnpv4gpMxNL2F1Yrx_l3U_Jt5GbMAN0Q"  # Replace with your Here API key
    URL = "https://discover.search.hereapi.com/v1/discover"
    query = 'hospitals'
    limit = 12

    PARAMS = {
        'apikey': api_key,
        'q': query,
        'limit': limit,
        'at': '{},{}'.format(latitude, longitude)
    }

    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    hospitals = data.get('items', [])

    return render(request, 'hospitals/result.html', {'hospitals': hospitals})





def donation_registration_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        guardians_contact = request.POST.get('guardians_contact')
        address = request.POST.get('address')

        # Create a new Donor object and save it to the database
        donor = Donor(
            full_name=full_name,
            email_address=email_address,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            guardians_contact=guardians_contact,
            address=address
        )
         
        donor.save()

        return redirect('success')  # Redirect to a success page

    return render(request, 'your_template_name.html')  # Replace with your actual template name



from django.db.models import Q

def last_five_entries(request):
    last_entries = Donor.objects.order_by('-id')[:5]  # Get the last five entries from the database
    
    search_query = request.GET.get('search')
    if search_query:
        search_results = Donor.objects.filter(
            Q(full_name__icontains=search_query.lower()) |
            Q(email_address__icontains=search_query.lower()) |
            Q(phone_number__icontains=search_query.lower()) |
            Q(date_of_birth__icontains=search_query.lower()) |
            Q(guardians_contact__icontains=search_query.lower()) |
            Q(address__icontains=search_query.lower())
        )
    else:
        search_results = None
    
    return render(request, 'last_entries.html', {'last_entries': last_entries, 'search_results': search_results})



# Create your views here.
