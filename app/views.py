from django.http import HttpResponse
from django.template import loader
from .models import Sport


def index(request):
    sports = Sport.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'sports': sports}))


def sport(request, sport_id):
    sport = Sport.objects.get(pk=sport_id)
    template = loader.get_template('sport.html')
    return HttpResponse(template.render({'sport': sport}))
