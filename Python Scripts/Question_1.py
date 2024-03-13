#Question 1 - How has the availability of substance use disorder treatment for children changed over time?
# Which quarters showed the most significant changes?

import matplotlib.pyplot as plt
import numpy as np

# Data for x-axis (quarters)
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019',
            'Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021',
            'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

# Data for y-axis 1 (Number of Responses)
responses = [180, 217, 204, 201, 146, 155, 75, 172, 126, 104, 90, 118, 77, 106, 133, 167, 132]

# Data for y-axis 2 (Percentage of Total Respondents)
percentages = [46, 69, 73, 58, 80, 76, 50, 79, 69, 50, 89, 67, 55, 60, 48, 67, 57]

# Create figure and axis objects
fig, ax1 = plt.subplots()

# Plotting the first y-axis
ax1.plot(quarters, responses, 'b-', label='Number of Responses')
ax1.set_xlabel('Quarters')
ax1.set_ylabel('Number of Responses', color='b')
ax1.tick_params('y', colors='b')

# Creating a second y-axis
ax2 = ax1.twinx()

# Plotting the second y-axis
ax2.plot(quarters, percentages, 'r-', label='Percentage of Total Respondents')
ax2.set_ylabel('Percentage of Total Respondents', color='r')
ax2.tick_params('y', colors='r')

# Displaying the legend for both y-axes
lines = ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [line.get_label() for line in lines])

# Rotating x-axis labels for better visibility
plt.xticks(rotation=45)

# Title of the graph
plt.title('Number of Responses and Percentage of Total Respondents')

# Display the line graph
plt.show()
