from django.shortcuts import render
from users.models import Profile
from django.contrib.auth.decorators import login_required
# from django.views.generic import DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    user = request.user
    context = {
       'profile':Profile.objects.filter(user=user).first()
    }

    return render(request, 'scago/home.html', context)

def aboutus(request):
    return render(request, 'scago/aboutus.html')

def contactus(request):
    return render(request, 'scago/contactus.html')


