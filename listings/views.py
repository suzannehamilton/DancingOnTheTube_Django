from django.shortcuts import render
from listings.models import Dance


def index(request):
    dances = Dance.objects.order_by('name')

    context = {'dances': dances}
    return render(request, 'listings/index.html', context)