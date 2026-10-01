import pygal

from die import Die

# initialize a six sided die
d6 = Die()
d6_2 = Die()

# roll the dice for a number of times and store results
results = [d6.roll() + d6_2.roll() for _ in range(1000)]

# analyze the resuls
frequencies = [results.count(side) for side in range(2, d6.num_sides + d6_2.num_sides + 1)]

# visualize results
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = [str(side) for side in range(2, d6.num_sides + d6_2.num_sides + 1)]
hist._x_title = "Result"
hist._y_title = 'Frequency of result'
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
