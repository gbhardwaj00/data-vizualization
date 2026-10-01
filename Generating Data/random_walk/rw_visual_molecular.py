import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))

plt.plot(rw.x_values, rw.y_values, linewidth = 1)

# emphasize start and end points
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

gca = plt.gca()
gca.get_xaxis().set_visible(False)
gca.get_yaxis().set_visible(False)

plt.show()
