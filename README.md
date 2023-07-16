# Sport_Analytic

> ## Models
> Country

> Stadium

> Coach

> Player

> Team

> Match

> Statistics

> Tournament

> Ranking


# Country
>> title


# Stadium
>> title

>> country m to 1

>> city

>> capacity 


# Coach
>> name

>> age

>> experience


# Player
>> name

>> age

>> position


# Team
>> title

>> country m to 1

>> home_stadium m to 1

>> foundation_year

>> type_sport

>> coach m to 1

>> team m to m


# Match
>> home_team

>> away_team

>> date

>> time

>> stadium m to 1


# Statistics
>> team m to 1

>> match m to 1

>> goals_scored

>> assists

>> hit_percent


# Tournament
>> title

>> date

>> team m to m


# Ranking
>> team m to 1

>> position

>> ranking_points