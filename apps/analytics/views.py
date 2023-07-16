from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet

# Create your views here.



def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'fotbal/index.html'
    # qs: QuerySet[Game] = Game.objects.all()
    return render(
        request=request,
        template_name=template_name,
        context={}
    )