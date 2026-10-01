import pygal

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

results = [die1.roll() + die2.roll() + die3.roll() for _ in range(50000)]

frequencies = [results.count(side) for side in range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1)]

hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice 50000 times"
hist.x_labels = [str(side) for side in range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1)]
hist._x_title = "Result"
hist._y_title = 'Frequency of result'
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_die.svg')