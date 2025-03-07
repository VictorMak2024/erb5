from django.shortcuts import render, get_object_or_404

# import class Listing from listings/models.py 
from . models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def listings(request):
    # .objects.all() -> take all data from databases
    """
    # listings = Listing.objects.filter() # In (), using QuerySet API
    # listings = Listing.objects.filter().exist()
    # print(listings)
    # listings = Listing.objects.get(id=1) # final record
    #print(listings)
    listings = Listing.objects.all()
    # print data from database
    print(list(listings))
    # print data from database
    for listing in listings:
        print(listing)"""
    #In Django, .order_by(param), .filter(param) <- Query Set (build sql command)
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)

#listings/urls.py <- urlpatterns
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')