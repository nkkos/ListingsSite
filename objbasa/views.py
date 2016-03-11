from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Listing
from .forms import NListing
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect



# Create your views here.
def post_list(request):
    lists = Listing.objects.filter(published_date__isnull = False).order_by('created_date')
    return render(request, 'basa/post_list.html', {'lists':lists})

def listing_detail(request, pk):
    Listo=get_object_or_404(Listing, pk=pk)
    return render(request, 'basa/listing_detail.html',{'Listing': Listo})

@login_required
def list_new(request):
    if request.method == "POST":
        form = NListing(request.POST)
        if form.is_valid():
            Listing = form.save(commit = False)
            Listing.author = request.user
            Listing.save()
            return redirect('objbasa.views.listing_detail', pk=Listing.pk)
    else:
        form = NListing()
    return render(request,'basa/list_edit.html', {'form':form})

@login_required
def list_edit(request, pk):
    Listo=get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = NListing(request.POST, instance=Listo)
        if form.is_valid():
            Listo = form.save(commit=False)
            Listo.author = request.user
            Listo.published_date = timezone.now()
            Listo.save()
            return redirect('objbasa.views.listing_detail', pk=Listo.pk)
    else:
        form = NListing(instance=Listo)
    return render(request, 'basa/list_edit.html', {'form': form})

@login_required
def list_draft_list(request):
    lists = Listing.objects.filter(published_date__isnull = True).order_by('created_date')
    return render(request, 'basa/list_draft_list.html', {'lists': lists})

@login_required
def list_publish(request, pk):
    Listo = get_object_or_404(Listing, pk=pk)
    Listo.publish()
    return redirect('objbasa.views.listing_detail', pk=pk )

@login_required
def list_remove(request, pk):
    Listo = get_object_or_404(Listing, pk=pk)
    Listo.delete()
    return redirect("objbasa.views.post_list")
