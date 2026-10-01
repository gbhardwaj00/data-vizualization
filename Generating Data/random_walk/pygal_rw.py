import pygal

from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

points = list(zip(rw.x_values, rw.y_values))

xy_chart = pygal.XY(stroke=True, show_dots=False, x_title='X', y_title='Y')
xy_chart.title = "Random Walk"
xy_chart.add('Path', points)
xy_chart.add('Start', [points[0]], stroke=False, show_dots=True, dots_size=4)
xy_chart.add('End', [points[-1]], stroke=False, show_dots=True, dots_size=4)
xy_chart.render_to_file('rw_pygal.svg')
