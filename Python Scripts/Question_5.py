import matplotlib.pyplot as plt

# Data for x-axis (quarters)
quarters = ["Q3 2018", "Q4 2018", "Q1 2019", "Q2 2019", "Q3 2019", "Q4 2019", "Q1 2020", "Q2 2020",
            "Q3 2020", "Q4 2020", "Q1 2021", "Q2 2021", "Q3 2021", "Q4 2021", "Q1 2022", "Q2 2022", "Q3 2022" ]

# Data for y-axis
total_places = [23932, 52024, 35121, 29787, 22249, 43905, 24756, 37075, 32583, 37051, 18178, 28485, 12586, 10779, 24267, 17684, 11366]
avg_places_per_resp = [69.8, 183.6, 142.8, 142.8, 288.9, 354.1, 272, 297, 316, 299, 249, 237, 146, 99, 237.9, 203.3, 133.7]
median_places = [11, 75, 30, 40, 12, 40, 25, 30, 30, 26, 48, 29, 40, 773, 9.5, 10, 21]
minimum = [0, 20, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0, 0, 0]
maximum = [10000, 9000, 6800, 5913, 7043, 7579, 10000, 9999, 10000, 9999, 8500, 9228, 2000, 1545, 418.8, 300, 200]

# Plotting the line graph
plt.plot(quarters, total_places, label="Total places")
plt.plot(quarters, avg_places_per_resp, label="Average places/respondent")
plt.plot(quarters, median_places, label="Median places")
plt.plot(quarters, minimum, label="Minimum")
plt.plot(quarters, maximum, label="Maximum")

# Adding labels and title
plt.xlabel("Quarters")
plt.ylabel("Number of Occupied Outpatient")
plt.title("Line Graph: Number of occupied outpatient treatment places, chairs, or openings")

# Adding a legend
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the graph
plt.show()
