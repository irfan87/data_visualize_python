# line graph
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 6, 30]

# change the style of the graph's background
plt.style.use('seaborn')

fig, ax = plt.subplots()

# change to the line to bold
ax.plot(input_values, squares, linewidth=3)

# set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# set size of tick labels
ax.tick_params(axis="both", labelsize=14)

ax.plot(squares)

# show the graph
plt.show()