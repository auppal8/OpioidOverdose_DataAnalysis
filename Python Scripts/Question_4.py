import matplotlib.pyplot as plt

# Data for x-axis (quarters)
quarters = ["Q3 2018", "Q4 2018", "Q1 2019", "Q2 2019", "Q3 2019", "Q4 2019", "Q1 2020", "Q2 2020",
            "Q3 2020", "Q4 2020", "Q1 2021", "Q2 2021", "Q3 2021", "Q4 2021", "Q1 2022", "Q2 2022", "Q3 2022" ]

# Data for y-axis
total_places = [588, 4250, 3610, 3206, 1895, 2955, 2168, 3104, 2898, 2364, 1389, 2449, 1462, 1172, 4160, 2705, 2774]
avg_places_per_resp = [57, 14.5, 14.2, 36.9, 35.8, 42.9, 34, 40, 42, 29, 43, 34, 23, 15, 44.3, 45.8, 47.8]
median_places = [10, 10, 15, 13, 14, 17, 11, 12, 17, 9.5, 15, 12, 10, 40, 22, 29, 29.5]
minimum = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 0, 0, 0]
maximum = [481, 368, 400, 408, 480, 400, 378, 408, 408, 408, 375, 400, 193, 79, 400, 100, 380]

# Plotting the line graph
plt.plot(quarters, total_places, label="Total places")
plt.plot(quarters, avg_places_per_resp, label="Average places/respondent")
plt.plot(quarters, median_places, label="Median places")
plt.plot(quarters, minimum, label="Minimum")
plt.plot(quarters, maximum, label="Maximum")

# Adding labels and title
plt.xlabel("Quarters")
plt.ylabel("Number of Occupied Beds")
plt.title("Line Graph: Number of Responses for Inpatient Beds")

# Adding a legend
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the graph
plt.show()
