from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.template import loader


class HomePageView(TemplateView):
    template_name = 'CarbAIWebApp/index.html'

class LoginPageView(TemplateView):
    template_name = 'CarbAIWebApp/login.html'


