from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(request):
    prof, searches_query = search_profile(request)
    context = {'profile': prof}
    return render(request, 'users/index.html', context)