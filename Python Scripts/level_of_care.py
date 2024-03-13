import matplotlib.pyplot as plt
import pandas as pd

# Data
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020',
            'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

# Create a DataFrame
data = pd.DataFrame({
    'quarters': quarters,
    'Outpatient – Individual': [49, 61, 62, 50, 75, 76, 61, 67, 67, 59, 86, 68, 57, 63, 68, 80, 80],
    'Outpatient – Group': [46, 51, 50, 44, 68, 68, 52, 60, 59, 54, 79, 62, 57, 57, 60, 70, 67],
    'Intensive Outpatient Program': [36, 37, 36, 28, 42, 45, 35, 40, 38, 34, 51, 41, 46, 40, 41, 44, 46],
    'Partial Hospitalization': [19, 12, 12, 10, 10, 13, 13, 14, 15, 13, 16, 16, 15, 11, 11, 14, 14],
    'Sober and Transitional Living': [14, 10, 10, 7, 10, 12, 13, 12, 12, 12, 12, 11, 14, 17, 16, 16, 14],
    'Group Home': [17, 12, 13, 10, 11, 11, 24, 13, 19, 20, 4, 18, 18, 19, 12, 9, 12],
    'Inpatient': [14, 15, 16, 11, 14, 17, 23, 17, 20, 17, 17, 16, 15, 16, 18, 13, 14],
    'Residential': [36, 27, 28, 24, 32, 28, 45, 36, 39, 38, 25, 45, 14, 45, 38, 29, 27],
    'Day Treatment': [15, 10, 11, 9, 13, 16, 14, 15, 16, 14, 18, 15, 21, 14, 18, 19, 21],
    'Detox': [11, 11, 12, 8, 13, 12, 12, 16, 12, 9, 12, 12, 15, 11, 13, 12, 15],
    'Emergency Medical Services': [3, 1, 2, 1, 2, 2, 1, 1, 2, 1, 3, 1, 1, 3, 1, 2, 1],
    'Self-help groups (AA/NA)': [17, 20, 16, 16, 28, 24, 22, 23, 23, 23, 24, 30, 28, 27, 28, 27, 28],
    'Peer Support Services': [18, 30, 27, 25, 41, 37, 35, 30, 32, 25, 37, 31, 35, 35, 41, 44, 44],
    '24 hour Crisis Services': [0, 0, 10, 9, 8, 16, 14, 13, 9, 7, 15, 9, 9, 10, 10, 12, 12]
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
