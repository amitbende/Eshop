from django.shortcuts import render
from .models import Eshop
from .forms import EshopForm
from .serializers import EshopSerializer
from rest_framework import viewsets

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class EshopDetails(viewsets.ModelViewSet):
    serializer_class = EshopSerializer
    queryset = Eshop.objects.all()

def Home_View(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)

class EshopView(ListView):
    model = Eshop
    queryset = Eshop.objects.all() 

class AddEshop(CreateView):
    model = Eshop
    fields = "__all__"
    success_url = reverse_lazy('showEshop_url')

class UpdateEshop(UpdateView):
    model = Eshop
    fields = "__all__"
    success_url = reverse_lazy('showEshop_url')

class DeleteEshop(DeleteView):
    model = Eshop
    fields = "__all__"
    success_url = reverse_lazy('showEshop_url')
    context_object_name = 'object_list'