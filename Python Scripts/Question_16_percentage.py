import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019',
            'Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021',
            'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

categories = ['Self-referred', 'Family or Friend', 'Employer', 'Health Plan/Insurance Company',
              'Primary Health Care Provider', 'Behavioral Health Care Provider', 'Hospital',
              'School', 'Church', 'Court', 'Corrections', 'Adult Probation',
              'Juvenile/Adolescent Probation', 'Department of Child Safety']

responses = {
    'Self-referred': [83, 86, 85, 227, 85, 87, 82, 82, 85, 88, 97, 89, 93, 87, 91, 86, 89],
    'Family or Friend': [80, 77, 75, 58, 74, 75, 73, 74, 76, 83, 82, 82, 86, 77, 85, 77, 87],
    'Employer': [63, 63, 60, 48, 60, 64, 61, 61, 62, 68, 78, 67, 74, 62, 66, 65, 81],
    'Health Plan/Insurance Company': [71, 76, 82, 62, 80, 85, 80, 79, 79, 77, 88, 84, 80, 80, 82, 82, 79],
    'Primary Health Care Provider': [83, 83, 85, 65, 83, 85, 87, 85, 83, 88, 88, 87, 89, 88, 85, 89, 78],
    'Behavioral Health Care Provider': [72, 78, 83, 71, 89, 92, 92, 92, 91, 0, 0, 0, 0, 0, 0, 0, 0],
    'Hospital': [76, 77, 76, 62, 79, 79, 80, 78, 79, 81, 81, 81, 81, 81, 83, 80, 70],
    'School': [50, 51, 54, 41, 54, 57, 47, 51, 50, 51, 61, 57, 59, 54, 53, 54, 68],
    'Church': [54, 51, 49, 42, 57, 60, 51, 55, 54, 58, 70, 61, 65, 61, 60, 56, 59],
    'Court': [59, 67, 66, 54, 70, 76, 70, 64, 69, 68, 79, 73, 74, 70, 76, 66, 59],
    'Corrections': [47, 59, 58, 52, 64, 67, 57, 57, 59, 57, 72, 67, 67, 58, 68, 62, 51],
    'Adult Probation': [53, 65, 63, 56, 69, 76, 69, 65, 68, 64, 78, 71, 72, 67, 74, 64, 49],
    'Juvenile/Adolescent Probation': [21, 33, 37, 32, 41, 38, 30, 40, 31, 26, 48, 37, 34, 29, 36, 37, 48],
    'Department of Child Safety': [0, 0, 47, 41, 52, 53, 40, 51, 47, 38, 66, 51, 51, 43, 48, 53, 33]
}

# Converting response data into a NumPy array
data = np.array([responses[category] for category in categories])

# Plotting the stacked bar graph
fig, ax = plt.subplots()
ax.bar(quarters, data[0], label=categories[0])

for i in range(1, len(categories)):
    ax.bar(quarters, data[i], bottom=np.sum(data[:i], axis=0), label=categories[i])

# Setting the labels and title
ax.set_xlabel('Quarters')
ax.set_ylabel('Percentage for Total Responses')
ax.set_title('Stacked Bar Graph')

# Rotating the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Adding a legend
ax.legend()

# Displaying the graph
plt.tight_layout()
plt.show()
