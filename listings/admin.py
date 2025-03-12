from django.contrib import admin

# Register your models here.
from django.forms import NumberInput
from django.db import models
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = 'id', 'title'
    # single tuple need add ,
    list_filter = 'realtor',
    #list_editable -> enable edit function
    list_editable = 'is_published','price'
    search_fields = 'title', 'description', 'address', 'price'
    list_per_page = 25
    ordering = 'id',
    #ordering = ['-id'] (desing order)
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': '10'})},
    }

admin.site.register(Listing,ListingAdmin)