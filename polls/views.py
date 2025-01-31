from django.http import HttpResponse


def index(request):
    return HttpResponse(" Him you are seeing my first django index ^-^.")
