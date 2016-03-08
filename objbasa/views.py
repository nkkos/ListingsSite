from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Listing

# Create your views here.
def post_list(request):
    lists = Listing.objects.all()
    return render(request, 'basa/post_list.html', {'lists':lists})

def listing_detail(request, pk):
    Listo=get_object_or_404(Listing, pk=pk)
    return render(request, 'basa/listing_detail.html',{'Listing': Listo})
