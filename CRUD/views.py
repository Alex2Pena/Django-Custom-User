from django.views.generic import ListView
from .models import Snack

class ListView(ListView):
    template_name = "CRUD/read-list.html"
    model = Snack


