from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Sauce, Food
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse



# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(View):

    
    def get(self, request):
        return HttpResponse("Sauce About")


class SauceList(TemplateView):
    template_name = "sauce_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sauces"] = Sauce.objects.all()
        return context
    
class SauceDetail(DetailView):
    model = Sauce
    template_name = "sauce_detail.html"

    
class SauceCreate(CreateView):
    model = Sauce
    fields = ['name', 'img', 'description']
    template_name = "sauce_create.html"
    def get_success_url(self):
        return reverse('sauce_detail', kwargs={'pk': self.object.pk})

    
class SauceUpdate(UpdateView):
    model = Sauce
    fields = ['name', 'img', 'description']
    template_name = "sauce_update.html"
    def get_success_url(self):
        return reverse('sauce_detail', kwargs={'pk': self.object.pk})

class SauceDelete(DeleteView):
    model = Sauce
    template_name = "sauce_delete_confirmation.html"
    success_url = "/sauces/"

