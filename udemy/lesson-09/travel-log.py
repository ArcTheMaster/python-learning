print('Enter a country:')
country = input() # Add country name

print('Add the number of visits done to this country:')
visits = int(input()) # Number of visits

print('Give a list of visited cities:')
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country=country, visits=visits, list_of_cities=list_of_cities) :
    # solution 1
    new_visit = {
        'country': country,
        'visits': visits,
        'cities': list_of_cities,
    }

    # solution 2
    # new_visit = {}
    # new_visit['country'] = country
    # new_visit['visits'] = visits
    # new_visit['cities'] = list_of_cities

    travel_log.append(new_visit)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")