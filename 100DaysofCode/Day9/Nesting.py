"""
100 DAYS OF CODE
DAY 9
"""
# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": {"Paris", "Lille", "Dijon", },
               "total_visits": {"Paris": 12, "Lille": 6, "Dijon": 2}},
    "Germany": {"cities_visited": {"Berlin", "Hamburg", "Stuttgart"},
                "total_visits": {"Berlin": 8, "Hamburg": 6, "Stuttgart": 1}}
}
for item in travel_log:
    print(item)
for item in travel_log:
    print(travel_log[item])
print(f'I visited France {travel_log["France"]["total_visits"]["Paris"]} times')

# Nesting a dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 20
     },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 15
    }
]

