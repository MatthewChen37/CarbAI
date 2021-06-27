from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Employee

from .forms import InputForm


class HomePageView(TemplateView):
    template_name = 'CarbAIWebApp/index.html'
    query = Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        query_results = Employee.objects.all()
        context.update({'query_results': query_results})
        return context



class LoginPageView(TemplateView):
    template_name = 'CarbAIWebApp/login.html'

class InputFormView(FormView):
    template_name = 'CarbAIWebApp/input.html' 
    form_class = InputForm 
    success_url = "/CarbAIWebApp"
    def get_context_data(self, **kwargs):
        context = super(InputFormView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form.save()
        return super(InputFormView, self).form_valid(form)



    