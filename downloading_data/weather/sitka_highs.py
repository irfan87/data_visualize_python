import os
import csv
from matplotlib import pyplot as pyplot
from datetime import datetime

filename = os.path.abspath('downloading_data/weather/data/sitka_weather_July_2018_simple.csv')

with open(filename) as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)

    # extract the Sitka's data to show the high temperature and dates
    dates, highs = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    # plot the high temperature
    pyplot.style.use('classic')
    fig, ax = pyplot.subplots()

    ax.plot(dates, highs, c='red')

    # format plot
    pyplot.title("Daily high temperatures, July 2018", fontsize=24)
    pyplot.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    pyplot.ylabel('Temperature (F)', fontsize=16)
    pyplot.tick_params(axis='both', which='major', labelsize=16)

    pyplot.show()