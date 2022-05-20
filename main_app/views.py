from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  items = Item.objects.all
  return render(request, 'home.html', {'items': items})

def about(request):
  return render(request, 'about.html')

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'