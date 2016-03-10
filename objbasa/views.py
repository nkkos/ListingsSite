from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Listing
from .forms import NListing

# Create your views here.
def post_list(request):
    lists = Listing.objects.all()
    return render(request, 'basa/post_list.html', {'lists':lists})

def listing_detail(request, pk):
    Listo=get_object_or_404(Listing, pk=pk)
    return render(request, 'basa/listing_detail.html',{'Listing': Listo})

def list_new(request):
    if request.method == "POST":
        form = NListing(request.POST)
        if form.is_valid():
            Listing = form.save(commit = False)
            Listing.author = request.user
            Listing.published_date = timezone.now()
            Listing.save()
            return redirect('objbasa.views.listing_detail', pk=Listing.pk)
    else:
        form = NListing()
    return render(request,'basa/list_edit.html', {'form':form})

def list_edit(request, pk):
    Listo = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = NListing(request.POST, instance=Listo)
        if form.is_valid():
            Listing = form.save(commit=False)
            Listing.author = request.user
            Listing.published_date = timezone.now()
            Listing.save()
            return redirect('objbasa.views.listing_detail', pk=Listing.pk)
    else:
        form = NListing(instance=Listo)
    return render(request, 'basa/list_edit.html', {'form': form})
