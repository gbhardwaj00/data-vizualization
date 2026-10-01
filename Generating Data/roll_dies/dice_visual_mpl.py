import matplotlib.pyplot as plt

from die import Die

# initialize two six sided dice
d6 = Die()
d6_2 = Die()

# roll the dice for a number of times and store results
results = [d6.roll() + d6_2.roll() for _ in range(1000)]

fig, ax = plt.subplots()
ax.hist(results, bins=range(2, d6.num_sides + d6_2.num_sides + 2),
        align='left', rwidth=0.8)

ax.set_title("Results of Rolling Two D6 Dice 1000 Times")
ax.set_xlabel("Result")
ax.set_ylabel("Frequency of Result")

plt.show()