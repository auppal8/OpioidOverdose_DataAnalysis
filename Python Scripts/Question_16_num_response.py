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
    'Self-referred': [318, 269, 240, 227, 153, 180, 123, 176, 154, 182, 99, 155, 128, 154, 252, 216, 207],
    'Family or Friend': [308, 243, 211, 198, 132, 155, 109, 158, 138, 172, 84, 144, 118, 137, 234, 200, 202],
    'Employer': [242, 197, 168, 165, 107, 131, 92, 131, 113, 141, 80, 117, 102, 109, 182, 163, 188],
    'Health Plan/Insurance Company': [271, 240, 230, 213, 144, 174, 120, 170, 143, 161, 90, 147, 111, 143, 227, 206, 184],
    'Primary Health Care Provider': [319, 261, 240, 222, 149, 175, 130, 182, 151, 184, 90, 152, 123, 157, 235, 224, 181],
    'Behavioral Health Care Provider': [277, 245, 235, 243, 160, 190, 138, 197, 165, 0, 0, 0, 0, 0, 0, 0, 0],
    'Hospital': [293, 241, 214, 211, 142, 162, 120, 168, 144, 170, 83, 142, 112, 144, 230, 200, 162],
    'School': [192, 159, 151, 140, 97, 116, 70, 110, 91, 107, 62, 100, 81, 97, 146, 136, 159],
    'Church': [206, 161, 139, 143, 102, 123, 77, 118, 99, 121, 71, 107, 90, 108, 166, 141, 137],
    'Court': [226, 209, 185, 183, 125, 157, 105, 139, 125, 142, 81, 127, 102, 124, 211, 166, 138],
    'Corrections': [181, 186, 163, 177, 115, 138, 86, 122, 108, 119, 73, 118, 92, 104, 187, 155, 119],
    'Adult Probation': [202, 205, 177, 192, 124, 157, 104, 140, 123, 133, 80, 125, 100, 119, 206, 161, 113],
    'Juvenile/Adolescent Probation': [79, 105, 104, 108, 74, 78, 45, 86, 57, 54, 49, 65, 47, 52, 100, 94, 112],
    'Department of Child Safety': [0, 0, 133, 139, 93, 108, 60, 110, 86, 80, 65, 89, 70, 76, 133, 134, 77]
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
ax.set_ylabel('Number of Responses')
ax.set_title('Stacked Bar Graph')

# Rotating the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Adding a legend
ax.legend()

# Displaying the graph
plt.tight_layout()
plt.show()
