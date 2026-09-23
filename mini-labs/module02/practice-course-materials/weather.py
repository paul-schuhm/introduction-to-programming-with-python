# Data: temperature records (given by a weather station)
temperatures = [
    {"date": "2026-03-01", "temperature": 12.5},
    {"date": "2026-03-02", "temperature": 14.0},
    {"date": "2026-03-03", "temperature": 9.8},
    {"date": "2026-03-04", "temperature": 20.2},
    {"date": "2026-03-05", "temperature": 15.1},
    {"date": "2026-03-06", "temperature": 11.4},
]

# Average temperature

# Stores the averate temperature (build step by step)
average_temp = 0

# Visit each temp, add to average_temp
for t in temperatures:
	print(t['temperature'])
	average_temp += t['temperature']

# average_temp = average_temp / len(temperatures)
average_temp /= len(temperatures)

print("Average temp = ", average_temp)
