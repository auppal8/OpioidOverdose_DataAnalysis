import matplotlib.pyplot as plt
import pandas as pd

# Data
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020',
            'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

# Create a DataFrame
data = pd.DataFrame({
    'quarters': quarters,
    'Substance Use Disorder Treatment': [66, 71, 72, 67, 88, 91, 80, 91, 89, 76, 96, 89, 0, 92, 86, 87, 85],
    'Dual Diagnosis/Co-Occurring': [54, 59, 59, 54, 74, 70, 70, 73, 71, 63, 76, 74, 0, 71, 67, 69, 68],
    'Intensive Outpatient Chemical Dependency Treatment': [35, 36, 34, 28, 38, 42, 30, 36, 36, 30, 52, 37, 0, 33, 33, 35, 36],
    'Mental Health': [48, 58, 55, 53, 76, 70, 70, 72, 70, 57, 74, 16, 0, 74, 72, 78, 79],
    'Trauma / PTSD': [45, 51, 47, 42, 69, 57, 59, 62, 57, 48, 67, 64, 0, 58, 61, 61, 65],
    'Residential': [37, 27, 29, 25, 31, 30, 44, 39, 40, 32, 24, 41, 0, 42, 38, 31, 29],
    'Day Treatment': [18, 13, 12, 11, 18, 22, 14, 19, 18, 18, 19, 20, 0, 21, 19, 21, 24],
    'Detox': [12, 14, 12, 11, 12, 17, 14, 18, 13, 11, 13, 13, 0, 12, 13, 14, 15],
    'Emergency Medical Services': [4, 2, 4, 2, 3, 3, 1, 4, 2, 2, 3, 3, 0, 3, 2, 3, 3],
    'Self-help groups (AA/NA)': [23, 22, 20, 19, 32, 28, 35, 29, 30, 29, 30, 38, 0, 37, 33, 29, 29],
    'Peer Support Services': [27, 34, 33, 30, 45, 45, 40, 41, 37, 35, 46, 42, 0, 45, 50, 46, 47],
    'Recreational Therapy': [0, 14, 11, 12, 19, 19, 22, 16, 23, 18, 16, 22, 0, 21, 22, 26, 20],
    'Occupational Therapy': [0, 7, 8, 7, 8, 7, 10, 9, 8, 9, 7, 7, 0, 10, 0, 0, 0],
    'Assisted Living': [0, 0, 4, 2, 1, 1, 5, 1, 2, 9, 1, 2, 0, 3, 0, 0, 0],
    'Skilled Nursing': [0, 0, 4, 2, 3, 2, 3, 2, 2, 5, 1, 1, 0, 3, 0, 0, 0],
    'Crisis Services': [0, 0, 14, 11, 17, 21, 19, 19, 14, 13, 19, 14, 0, 15, 20, 21, 20],
    'Medication Assisted Treatment': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 33, 38]
})

colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon']

# Set up the figure and axis
fig, axes = plt.subplots(nrows=3, ncols=6, figsize=(13, 13))
axes = axes.flatten()

# Plot donut chart for each quarter
for i, quarter in enumerate(quarters):
    quarter_data = data.loc[data['quarters'] == quarter].drop(columns='quarters').squeeze()
    if i == 0:
        wedges, text = axes[1].pie(quarter_data, colors=colors, startangle=90, wedgeprops={'width': 0.4})
        axes[1].set_title(quarter)
        axes[0].legend(wedges, quarter_data.index, loc='center')
    else:
        wedges, text = axes[i + 1].pie(quarter_data, colors=colors, startangle=90, wedgeprops={'width': 0.4})
        axes[i + 1].set_title(quarter)

axes[0].axis('off')  # Hide the empty subplot
# axes[18].axis('off')  # Hide the empty subplot
# axes[19].axis('off')  # Hide the empty subplot


# Adjust the plot layout
plt.tight_layout()
plt.show()
