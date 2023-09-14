import datetime
import random

from django.db import models

# Create your models here.


class Country(models.Model):
    """Country model."""

    title = models.CharField(
        verbose_name='название',
        max_length=250,
        unique=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self) -> str:
        return self.title
    

class Stadium(models.Model):
    """Stadium model."""

    title = models.CharField(
        verbose_name='название',
        max_length=130,
        unique=True
    )
    country = models.ForeignKey(
        verbose_name='страна',
        to=Country,
        on_delete=models.CASCADE,
        related_name='country_stadium'
    )
    city = models.CharField(
        verbose_name='город',
        max_length=130,
        unique=True
    )
    capacity = models.IntegerField(
        verbose_name='вместимость',
        default=5000
    )

    class Meta:
        ordering = ('capacity',)
        verbose_name = 'стадион'
        verbose_name_plural = 'стадионы'

    def __str__(self) -> str:
        return self.title
    
    
class Coach(models.Model):
    """Coach model."""

    name = models.CharField(
        verbose_name='имя',
        max_length=130
    )
    age = models.IntegerField(
        verbose_name='возраст'
    )
    experience = models.IntegerField(
        verbose_name='опыт'
    )

    class Meta:
        ordering = ('-experience',)
        verbose_name = 'тренер'
        verbose_name_plural = 'тренеры'

    def __str__(self) -> str:
        return f'{self.name} возраст {self.age} лет'


class Player(models.Model):
    """Player model."""

    name = models.CharField(
        verbose_name='имя',
        max_length=130
    )
    age = models.IntegerField(
        verbose_name='возраст'
    )
    position = models.CharField(
        verbose_name='позиция',
        max_length=130
    )
    # team = models.ForeignKey(
    #     verbose_name='команда',
    #     to=Team,
    #     on_delete=models.CASCADE,
    #     related_name='team_player'
    # )

    class Meta:
        ordering = ('id',)
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def __str__(self) -> str:
        return f'{self.name} возраст {self.age} >> {self.position}'
    


class Team(models.Model):
    """Team model."""

    title = models.CharField(
        verbose_name='название',
        max_length=250,
        unique=True
    )
    country = models.ForeignKey(
        verbose_name='страна',
        to=Country,
        on_delete=models.CASCADE,
        related_name='country_of_team'
    )
    home_stadium = models.OneToOneField(
        verbose_name='домашний стадион',
        to=Stadium,
        on_delete=models.CASCADE,
        related_name='teams_stadium'
    )
    foundation_year = models.DateField(
        verbose_name='дата создания',
        default=datetime.datetime.today() - datetime.timedelta(
            days=random.randint(22,222)
        )
    )
    type_sport = models.CharField(
        verbose_name='вид спорта',
        max_length=120
    )
    coach = models.OneToOneField(
        verbose_name='тренер',
        to=Coach, 
        on_delete=models.CASCADE,
        related_name='team_coach'
    )
    player = models.ManyToManyField(
        verbose_name='игрок',
        to=Player,
        related_name='players_command'
    )


    class Meta:
        ordering = ('type_sport',)
        verbose_name = 'команда'
        verbose_name_plural = 'команды'

    def __str__(self) -> str:
        return f'Команда {self.title} спорт {self.type_sport}' 
    

class Match(models.Model):
    """Matches model."""

    home_team = models.ForeignKey(
        verbose_name='домашняя команда',
        to=Team,
        on_delete=models.CASCADE,
        related_name='team_home'
    )
    away_team = models.ForeignKey(
        verbose_name='выездная команда',
        to=Team,
        on_delete=models.CASCADE,
        related_name='team_away'
    )
    date = models.DateField(
        verbose_name='дата матча',
        auto_now_add=True
    )
    time = models.TimeField(
        verbose_name='время начала игры',
        auto_now_add=True
    )
    stadium = models.ForeignKey(
        verbose_name='стадион',
        to=Stadium,
        on_delete=models.CASCADE,
        related_name='match_on_stadium'
    )
    is_favorite = models.BooleanField(
        verbose_name='избранное',
        default=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'матч'
        verbose_name_plural = 'матчи'

    def __str__(self) -> str:
        return f'Команда {self.home_team.title} против {self.away_team.title}'
    

class Statistics(models.Model):
    """Statistics player match model."""

    team = models.ForeignKey(
        verbose_name='команда',
        to=Team, 
        on_delete=models.CASCADE,
        related_name='command_statistic'
    )
    match = models.ForeignKey(
        verbose_name='матч',
        to=Match, 
        on_delete=models.CASCADE,
        related_name='statistics_match_team'
    )
    goals_scored = models.IntegerField(
        verbose_name='забито мячей'
    )
    assists = models.IntegerField(
        verbose_name='сделано асистов'
    )
    hit_percent = models.DecimalField(
        verbose_name='процент попадания',
        decimal_places=2,
        max_digits=5
    )

    class Meta:
        ordering = ('goals_scored',)
        verbose_name = 'статистика'
        verbose_name_plural = 'статистика'

    def __str__(self) -> str:
        return f'матч {self.match.home_team} против {self.match.away_team}'


class Tournament(models.Model):
    """Coach model."""

    title = models.CharField(
        verbose_name='название',
        max_length=130
    )
    date = models.DateField(
        verbose_name='дата проведения',
        auto_now_add=True
    )
    team = models.ManyToManyField(
        verbose_name='команда',
        to=Team,
        related_name='teams_on_tournament'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'турнир'
        verbose_name_plural = 'турниры'

    def __str__(self) -> str:
        return self.title
    

class Ranking(models.Model):
    """Coach model."""

    team = models.ForeignKey(
        verbose_name='команда',
        to=Team,
        on_delete=models.CASCADE,
        related_name='teams_ranking'
    )
    position = models.IntegerField(
        verbose_name='позиция'
    )
    ranking_points = models.IntegerField(
        verbose_name='очки команд'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'

    def __str__(self) -> str:
        return self.team.title