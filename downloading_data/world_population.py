import json

from pygal_maps_world.maps import World
from pygal.style import RotateStyle, LightColorizedStyle    

from country_codes import get_country_code

from pygal_maps_world.i18n import COUNTRIES

# load data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# build a dictionary of population data for 2010
populations_2010 = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        # only add if the code is not None
        if code:
            populations_2010[code] = population

# check which countries from pygal were not found in the population data
for cc, name in COUNTRIES.items():
    if cc not in populations_2010:
        print(f"{name} ({cc}) not found in population data")

# divide the countries into 3 population levels
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in populations_2010.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# see how many countries are in each level
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')