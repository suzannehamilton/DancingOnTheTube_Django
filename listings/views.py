from django.http import HttpResponse
from listings.models import Dance


def index(request):
    dances = Dance.objects.order_by('name')
    output = ', '.join([dance.name for dance in dances])
    return HttpResponse(output)