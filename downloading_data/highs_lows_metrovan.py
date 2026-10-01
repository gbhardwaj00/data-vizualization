import csv
from datetime import datetime
import matplotlib.pyplot as plt

# get avg. temp of metro vancouver cities for 2025

cities = {
    'Vancouver': 'vancouver_weather_2025.csv',
    'Burnaby': 'burnaby_weather_2025.csv',
    'Delta': 'delta_weather_2025.csv',
    # 'Richmond': 'richmond_weather_2025.csv'
}


def read_city_weather(city, filename):
    dates, highs, lows, avgs = [], [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header row

        for row in reader:
            try:
                date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
                avg = float(row[1])
                low = float(row[2])
                high = float(row[3])
            except ValueError:
                print(f"Missing data for {row[0]} for {city} ")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
                avgs.append(avg)

    return dates, highs, lows, avgs


city_data = {
    city: read_city_weather(city, filename)
    for city, filename in cities.items()
}


def rolling_average(values, window=7):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window // 2) 
        end = min(len(values), i + window // 2 + 1)
        smoothed.append(sum(values[start:end]) / (end - start))
    return smoothed


# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
for city in cities.keys():
    temp_data = city_data.get(city)
    smoothed_avgs = rolling_average(temp_data[3], window=7)
    plt.plot(temp_data[0], smoothed_avgs, label=city)
plt.legend()

# format plot
plt.title("Average Temperature in Metro Vancouver Cities (2025)", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()