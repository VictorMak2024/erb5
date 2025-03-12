from django.shortcuts import render, get_object_or_404

# import class Listing from listings/models.py 
from . models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from listings.choices import price_choices, bedroom_choices, district_choices

# Create your views here.

# def listings_2(request):
#     Listings = Listing.objects.filter(Q(district='tst')|Q(district='mk'))

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
    #listings = Listing.objects.filter(district=F('address')) # filter 'address' using F() expression
    #listings = Listing.objects.filter(Q(district='tst')|Q(district='mk')) # filter district using Q() object
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
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) #lte -> less than or equal to
    context = {
        'price_choices' : price_choices,
        'district_choices' : district_choices,
        'bedroom_choices' : bedroom_choices,
        'listings' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context)