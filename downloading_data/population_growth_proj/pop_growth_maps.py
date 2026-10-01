import sys
import requests
import json

from pygal_maps_world.maps import World
from pygal.style import Style

# call the api to obtain the required data 
url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.GROW?date=2023:2025&format=json&per_page=1000"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve data: {e}")
    sys.exit(1)

print("Success")

# save the data to a JSON file just to have a copy of it for reference
with open('./population_growth_data.json', 'w') as f:
    json.dump(data, f, indent=4)

pop_data = data[1]  # The actual data is in the second element of the list

# build dictionaries of population growth data for 2023, 2024, and 2025
pop_growth_2023 = {}
pop_growth_2024 = {}
pop_growth_2025 = {}

# process the data and populate the dictionaries with country codes and growth values
for pop_dict in pop_data:
    year = pop_dict["date"]
    code = pop_dict["country"]["id"].lower()
    growth_value = float(pop_dict["value"]) if pop_dict["value"] is not None else 0.0
    if year == "2023":
        pop_growth_2023[code] = growth_value
    elif year == "2024":
        pop_growth_2024[code] = growth_value
    elif year == "2025":
        pop_growth_2025[code] = growth_value

def divide_growth_levels(pop_growth_dict):
    """Divide the countries into 4 population growth levels for better visualization"""
    pop_growth_neg, pop_growth_low, pop_growth_medium, pop_growth_high = {}, {}, {}, {}
    for cc, growth in pop_growth_dict.items():
        if growth < 0:
            pop_growth_neg[cc] = growth
        elif growth < 1.0:
            pop_growth_low[cc] = growth
        elif growth < 2.0:
            pop_growth_medium[cc] = growth
        else:
            pop_growth_high[cc] = growth
    return pop_growth_neg, pop_growth_low, pop_growth_medium, pop_growth_high

# divide the countries into 3 population growth levels for 2023 for better visualization
pop_growth_neg_2023, pop_growth_2023_low, pop_growth_2023_medium, pop_growth_2023_high = divide_growth_levels(pop_growth_2023)
pop_growth_neg_2024, pop_growth_2024_low, pop_growth_2024_medium, pop_growth_2024_high = divide_growth_levels(pop_growth_2024)
pop_growth_neg_2025, pop_growth_2025_low, pop_growth_2025_medium, pop_growth_2025_high = divide_growth_levels(pop_growth_2025)

# create world maps for each year using pygal
wm_style = Style(colors=('#d73027', '#fee08b', '#91cf60', "#891a98"))

def create_world_map(title, pop_growth_neg, pop_growth_low, pop_growth_medium, pop_growth_high):
    """Create a world map for the given population growth data"""
    wm = World(style=wm_style)
    wm.title = title
    wm.add('Negative', pop_growth_neg)
    wm.add('<1%', pop_growth_low)
    wm.add('1%-2%', pop_growth_medium)
    wm.add('>2%', pop_growth_high)
    return wm

wm_2023 = create_world_map('Population Growth in 2023, by Country', pop_growth_neg_2023, pop_growth_2023_low, pop_growth_2023_medium, pop_growth_2023_high)

wm_2024 = create_world_map('Population Growth in 2024, by Country', pop_growth_neg_2024, pop_growth_2024_low, pop_growth_2024_medium, pop_growth_2024_high)

wm_2025 = create_world_map('Population Growth in 2025, by Country', pop_growth_neg_2025, pop_growth_2025_low, pop_growth_2025_medium, pop_growth_2025_high)



# save the maps to SVG files
wm_2023.render_to_file('pop_growth_2023.svg')
wm_2024.render_to_file('pop_growth_2024.svg')
wm_2025.render_to_file('pop_growth_2025.svg')