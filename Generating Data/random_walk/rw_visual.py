import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making random walks until cancelled
while True:
    # make a random walk and plot the points
    rw = RandomWalk(1000000)
    rw.fill_walk()

    # to color points according to their position
    point_numbers = list(range(rw.num_points))

    plt.figure(figsize=(10,6))
    # general main walk
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
                s = 1, edgecolors='none')

    #emphasize end points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100) 
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove axes
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # preview graph
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break

