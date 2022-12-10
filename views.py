from django.shortcuts import render

# Create your views here.
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')  # getting our template
    # rendering the template in HttpResponse
    return HttpResponse(template.render())
