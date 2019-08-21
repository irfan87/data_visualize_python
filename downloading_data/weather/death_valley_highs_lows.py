import os
import csv
from matplotlib import pyplot as pyplot
from datetime import datetime

filename = os.path.abspath('downloading_data/weather/data/death_valley_2018_simple.csv')

with open(filename) as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)

    # extract the Sitka's data to show the high temperature and dates
    dates = []
    highs = []
    lows = []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # plot the high temperature
    pyplot.style.use('classic')
    fig, ax = pyplot.subplots()

    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')

    # shading between highs and lows chart
    pyplot.fill_between(dates, highs, lows, facecolor='magenta', alpha=0.1)

    # format plot
    pyplot.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=20)
    pyplot.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    pyplot.ylabel('Temperature (F)', fontsize=16)
    pyplot.tick_params(axis='both', which='major', labelsize=16)

    pyplot.show()