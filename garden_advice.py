# garden_advice.py
# An app that provides gardening tips based on the current month and season.

# TODO: Replace hardcoded month number with dynamic input from the user
month = 3

# TODO: Refactor the season logic into a separate function called get_season(month)
if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
else:
    season = "Autumn"

# TODO: Refactor the advice logic into a separate function called get_advice(season)
if season == "Winter":
    advice = "Protect your plants from frost. Consider indoor gardening."
elif season == "Spring":
    advice = "Great time to plant seeds! Make sure to water regularly."
elif season == "Summer":
    advice = "Water your plants early in the morning to avoid evaporation."
else:
    advice = "Harvest remaining crops and prepare soil for winter."

# TODO: Add a docstring to document what this program does
print(f"Month: {month}")
print(f"Season: {season}")
print(f"Gardening tip: {advice}")
