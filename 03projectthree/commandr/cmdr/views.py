from django.views.generic import ListView
from .models import cmdr

class HomePageView(ListView):
    model = cmdr
    template_name='home.html'
