import pygal

from die import Die

# initialize a six sided die
d6 = Die()

# roll the die for a no of times and store results
results = [d6.roll() for _ in range(1000)]

# analyze the resuls
frequencies = [results.count(side) for side in range(1, d6.num_sides + 1)]

# visualize results
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(side) for side in range(1, d6.num_sides + 1)]
hist._x_title = "Result"
hist._y_title = 'Frequency of result'
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
