"""
garden_advice.py
An app that provides gardening tips based on the current month
and season. Provides advice based on the season determined
from the given month.
TODO: Replace hardcoded month number with dynamic input from the user
"""

month = 3


def get_season(month):
    """
    Return the season name based on the given month number.
    """
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"


def get_advice(season):
    """
    Return gardening advice based on the given season.
    """
    if season == "Winter":
        advice = (
            "Protect your plants from frost. "
            "Consider indoor gardening."
        )
    elif season == "Spring":
        advice = (
            "Great time to plant seeds! "
            "Make sure to water regularly."
        )
    elif season == "Summer":
        advice = (
            "Water your plants early in the morning "
            "to avoid evaporation."
        )
    else:
        advice = (
            "Harvest remaining crops and "
            "prepare soil for winter."
        )
    return advice


season = get_season(month)
advice = get_advice(season)

print(f"Month: {month}")
print(f"Season: {season}")
print(f"Gardening tip: {advice}")
