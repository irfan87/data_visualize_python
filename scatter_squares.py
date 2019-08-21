import matplotlib.pyplot as pyplot

pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()

# calculate data automatically
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# set the x and y values with scatter value is 10 and set the colormap to identify minimum values and maximum values from y_values
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=pyplot.cm.Greens)

# set title pf x and y axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of values", fontsize=14)

# set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# set size of tick params
ax.tick_params(axis='both', which='major', labelsize=14)

pyplot.show()

# save the figure as .png 
# pyplot.savefig('squares_plot.png', bbox_inches='tight')
