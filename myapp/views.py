from django.shortcuts import render, HttpResponse
from .models import LegoSet

# Create your views here.
def home(request):
    return render(request, "home.html")

def sets(request):
    context = {}
    lego_sets = LegoSet.objects.all()
    context['sets'] = lego_sets
    return render(request, "sets.html", context)