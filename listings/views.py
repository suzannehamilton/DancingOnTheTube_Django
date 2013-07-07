from django.shortcuts import render
from listings.models import Dance
# from schedule.models import Calendar


def index(request):
    dances = Dance.objects.order_by('name')
    # cal = Calendar.objects.get()

    context = {'dances': dances}
    return render(request, 'listings/index.html', context)