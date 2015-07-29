from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404

from .models import Acronym

# Create your views here.

def index(request):
    latest_acronym_list = Acronym.objects.order_by('-pub_date')[:5]
    context = {'latest_acronym_list': latest_acronym_list}
    return render(request, 'acronym/index.html', context)

def detail(request, acronym_id):
    acronym = get_object_or_404(Acronym, pk=acronym_id)
    return render(request, 'acronym/detail.html', {'acronym': acronym})
