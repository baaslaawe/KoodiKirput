# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {    }
    return HttpResponse(template.render(context, request))

# Create your views here.
