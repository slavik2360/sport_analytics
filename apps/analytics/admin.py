from django.contrib import admin

# Register your models here.

from .models import (
    Country,
    Stadium,
    Coach,
    Team,
    Player,
    Match,
    Statistics,
    Tournament,
    Ranking
)

admin.site.register(Country)
admin.site.register(Stadium)
admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Statistics)
admin.site.register(Tournament)
admin.site.register(Ranking)