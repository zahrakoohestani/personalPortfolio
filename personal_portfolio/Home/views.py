from django.shortcuts import render
from .models import home_page
from .models import about_me

def home(request):
    project = home_page.objects.all()
    about_me_data = about_me.objects.all()
    return render(request, 'Home/home.html', {'project' : project , 'about_me_data' : about_me_data})