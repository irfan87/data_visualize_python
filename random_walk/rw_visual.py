from matplotlib import pyplot as pyplot
from random_walk import RandomWalk

# keep making new values, as long as the program active
while True:
    # make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # plot the points in the walk
    pyplot.style.use('classic')
    fig, ax = pyplot.subplots(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=75, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=75, zorder=2)

    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=pyplot.cm.Blues, edgecolors='none', s=1)

    # cleaning the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    pyplot.show()

    keep_running = input("Make another walk? (y/n): ")

    if keep_running == 'n':
        break