# Python
from typing import Any

# Django

from django.http.request import HttpRequest
from django.http.response import (
    HttpResponse,
    JsonResponse
)
from django.db.models.query import QuerySet
from django.views.generic import View
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.utils import timezone
# Create your views here.

from .models import Match


class MainView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'sports/index.html'
        today = timezone.now().date()
        matches: QuerySet = Match.objects.filter(date=today)
        return render(
            request=request,
            template_name=template_name,
            context={
                'matches': matches
            }
        )

class ToggleFavoriteView(View):

    def post(self, request: HttpRequest, match_id):
        match = Match.objects.get(pk=match_id)

        match.is_favorite = not match.is_favorite
        match.save()

        return JsonResponse({'success': True})
