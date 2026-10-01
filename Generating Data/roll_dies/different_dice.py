import pygal

from die import Die

# initialize a six sided die and a ten sided die
d6 = Die()
d10 = Die(10)

# roll the dice for a number of times and store results
results = [d6.roll() + d10.roll() for _ in range(50000)]

# analyze the resuls
frequencies = [results.count(side) for side in range(2, d6.num_sides + d10.num_sides + 1)]

# visualize results
hist = pygal.Bar()
hist.title = "Results of rolling one D6 and one D10 50000 times"
hist.x_labels = [str(side) for side in range(2, d6.num_sides + d10.num_sides + 1)]
hist._x_title = "Result"
hist._y_title = 'Frequency of result'
hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')
