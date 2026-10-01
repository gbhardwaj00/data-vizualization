from pygal_maps_world.i18n import COUNTRIES

# maps pygal's country name to the name used in population_data.json,
# for countries where the World Bank data uses a different name
PYGAL_NAME_TO_JSON_NAME = {
    'Bolivia, Plurinational State of': 'Bolivia',
    'Congo, the Democratic Republic of the': 'Congo, Dem. Rep.',
    'Congo': 'Congo, Rep.',
    'Egypt': 'Egypt, Arab Rep.',
    'Gambia': 'Gambia, The',
    'Hong Kong': 'Hong Kong SAR, China',
    'Iran, Islamic Republic of': 'Iran, Islamic Rep.',
    'Kyrgyzstan': 'Kyrgyz Republic',
    "Korea, Democratic People's Republic of": 'Korea, Dem. Rep.',
    'Korea, Republic of': 'Korea, Rep.',
    "Lao People's Democratic Republic": 'Lao PDR',
    'Libyan Arab Jamahiriya': 'Libya',
    'Moldova, Republic of': 'Moldova',
    'Macedonia, the former Yugoslav Republic of': 'Macedonia, FYR',
    'Macao': 'Macao SAR, China',
    'Palestine, State of': 'West Bank and Gaza',
    'Slovakia': 'Slovak Republic',
    'Tanzania, United Republic of': 'Tanzania',
    'Venezuela, Bolivarian Republic of': 'Venezuela, RB',
    'Viet Nam': 'Vietnam',
    'Yemen': 'Yemen, Rep.',
}
JSON_NAME_TO_PYGAL_NAME = {v: k for k, v in PYGAL_NAME_TO_JSON_NAME.items()}

def get_country_code(country_name):
    """return the pygal country code for the given country, if available"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # try the json-to-pygal name override, for countries with different names
    pygal_name = JSON_NAME_TO_PYGAL_NAME.get(country_name)
    if pygal_name:
        for code, name in COUNTRIES.items():
            if name == pygal_name:
                return code
    
    # if country not found, return None
    return None

def get_countries_not_found_in_data(populations_2010):
    """return a list of countries not found in the population data"""
    countries_not_found = []
    for cc, name in COUNTRIES.items():
        if cc not in populations_2010:
            countries_not_found.append(name)            
    return countries_not_found
