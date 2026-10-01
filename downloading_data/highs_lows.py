import csv
from matplotlib import pyplot as plt
from datetime import datetime

# get dates, highs, lows temperatures from the file
death_valley = 'death_valley_2014.csv'
sitaka = 'sitka_weather_2014.csv'
vancouver = 'vancouver_weather_2025.csv'

filename = vancouver
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs , lows, dates = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            high = float(row[3])
            low = float(row[2])
        except ValueError:
            print(f"Missing data for {row[0]}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, label='High')
plt.plot(dates, lows, c='blue', alpha=0.5, label='Low')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.legend()

# format plot
plt.title('Daily High and Low Temperatures - 2025\nVancouver, BC', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()