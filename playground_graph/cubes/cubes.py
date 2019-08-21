import matplotlib.pyplot as pyplot

# graph's background style
pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()

# define the values of the cubes
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

ax.scatter(x_values, cubes, s=10, c=cubes, edgecolor='none', cmap=pyplot.cm.Blues)

# chart and label title
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis="both", labelsize=14)

ax.axis([0, 5100, 0, 5100**3])

pyplot.show()