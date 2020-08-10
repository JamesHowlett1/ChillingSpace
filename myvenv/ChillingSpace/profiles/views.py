from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Profile

# Create your views here.
def home_view(request):
    user = request.user
    hello = "Hello, world!"

    context = {
        'user': user,
        'hello': hello,
    }

    return render(request, 'profiles/home.html', context)

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile,
    }

    return render(request,'profiles/my_profile.html', context)

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)
