from django.shortcuts import render

# import class Listing from listings/models.py 
from . models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def listings(request):
    # .objects.all() -> take all data from databases
    #listings = Listing.objects.all()
    #In Django, .order_by(param), .filter(param) <- Query Set (build sql command)
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)

#listings/urls.py <- urlpatterns
def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')