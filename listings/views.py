from django.http import HttpResponse
from django.template import loader, RequestContext
from listings.models import Dance


def index(request):
    dances = Dance.objects.order_by('name')
    template = loader.get_template('listings/index.html')
    context = RequestContext(request, {
        'dances': dances,
    })
    return HttpResponse(template.render(context))