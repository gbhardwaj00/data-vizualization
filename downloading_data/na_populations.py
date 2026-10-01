from pygal_maps_world.maps import World

wm = World()
wm.title = 'Populations of North America Countries'

wm.add('North America', {'ca': 36624199, 'mx': 113423047, 'us': 324459463})
wm.render_to_file('na_populations.svg')
