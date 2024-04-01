# nested list
travel_log = {
    'France': {
        'visited_cities': ['Paris', 'Caen', 'Rochefort', 'La Rochelle', 'Rennes'],
        'visit_count': 35,
    },
    'Germany': {
        'visited_cities': ['Desden', 'Stuttgart'],
        'visit_count': 1,
    }
}

print(travel_log)

# dictionary nested inside a list
travel_log = [
    {
        'country': 'France', 
        'visited_cities': ['Paris', 'Caen', 'Rochefort', 'La Rochelle', 'Rennes'], 
        'visit_count': 35,
    },
    {
        'country': 'Germany', 
        'visited_cities': ['Desden', 'Stuttgart'], 
        'visit_count': 1,
    },
]

for travel in travel_log :
    print(travel)

