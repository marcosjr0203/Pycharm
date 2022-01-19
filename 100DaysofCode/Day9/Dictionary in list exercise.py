"""
100 DAYS OF CODE
DAY 9
TODO-1 Write a function that adds to travel_log a new country, how many times it was visited and list of cities.
"""
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


def add_new_country(ctr, vst, tot):
    new_country = {"country": ctr, "cities_visited": vst, "total_visits": tot}
    travel_log.append(new_country)


country = input("Inform country: ")
cities_visited = input("Inform the visited cities: ").split(", ")
total_visits = int(input("Inform the total of visits: "))
add_new_country(ctr=country, vst=cities_visited, tot=total_visits)
print(travel_log)