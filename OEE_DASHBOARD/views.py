from re import template
from django.shortcuts import render #legacy unsure if needed
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class DA5PageView(TemplateView):
    template_name = 'da5.html'

class DA6PageView(TemplateView):
    template_name = 'da6.html'

class BB1PageView(TemplateView):
    template_name = 'bb1.html'

class BB2PageView(TemplateView):
    template_name = 'bb2.html'