import pygal

from die import Die

# initialize two six sided dice
d6 = Die()
d6_2 = Die()

# roll the dice for a number of times and store multiplication results
results = [d6.roll() * d6_2.roll() for _ in range(1000)]

# for possible products, avoid recounting in frequency
products = sorted({i * j for i in range(1, d6.num_sides + 1) 
                   for j in range(1, d6_2.num_sides + 1)})
# analyze the resuls
frequencies = [results.count(p) for p in products]

# visualize results
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times and multiplying their results"
hist.x_labels = [str(p) for p in products]
hist._x_title = "Result"
hist._y_title = 'Frequency of result'
hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_multiply_visual.svg')
