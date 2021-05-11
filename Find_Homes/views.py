from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Listing, Location
from django.forms import modelformset_factory
from .forms import ListingForm, LocationForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def find_home(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', False)
        listings = Listing.objects.filter(
            location__zip_code__contains=searched)

        return render(request, 'searchListings.html', {'searched': searched, 'listings': listings})
    else:
        return render(request, 'searchListings.html', {})


def create_listing(request):

    if request.method == 'POST':
        form1 = ListingForm(request.POST, request.FILES)
        form2 = LocationForm(request.POST)
        if form1.is_valid() and form2.is_valid():

            # listing.images = form1.cleaned_data['images']
            listing_instance = form1.save(commit=False)
            location_instance = form2.save(commit=False)
            listing_instance.location = location_instance
            location_instance.save()
            listing_instance.save()
            form1 = ListingForm()
            form2 = LocationForm()
            return redirect('/')
    else:
        form1 = ListingForm()
        form2 = LocationForm()

    return render(request, 'createListing.html', {'form1': form1, 'form2': form2})


def edit_listing(request):
    if request.method == 'GET':
        listings = Listing.objects.all()

        return render(request, 'allListings.html', {'listings': listings})
    return render(request, 'allListings.html', {})


def update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    location = Location.objects.get(id=listing.location.id)
    form1 = ListingForm(instance=listing)
    form2 = LocationForm(instance=location)
    if request.method == 'POST':
        form1 = ListingForm(request.POST, request.FILES, instance=listing)
        form2 = LocationForm(request.POST, instance=location)
        if form1.is_valid() and form2.is_valid():

            # listing.images = form1.cleaned_data['images']
            listing_instance = form1.save(commit=False)
            location_instance = form2.save(commit=False)
            listing_instance.location = location_instance
            location_instance.save()
            listing_instance.save()
            form1 = ListingForm()
            form2 = LocationForm()
            return redirect('/')

    return render(request, 'createListing.html', {'form1': form1, 'form2': form2})


def delete_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    location = Location.objects.get(id=listing.location.id)

    if request.method == 'POST':
        listing.delete()
        location.delete()
        return redirect('/')
    return render(request, 'delete.html', {'item': listing})


def get_home(request, pk):
    listing = Listing.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'Listing.html', {'listing': listing})
