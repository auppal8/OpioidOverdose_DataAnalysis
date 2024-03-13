import matplotlib.pyplot as plt
import pandas as pd

# Data
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020',
            'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

# Create a DataFrame
data = pd.DataFrame({
    'quarters': quarters,
    '0-11 years': [23, 38, 41, 31, 40, 43, 25, 43, 37, 25, 46, 32, 25, 31, 16, 25, 22],
    '12-17 years': [23, 31, 32, 27, 40, 33, 25, 36, 32, 25, 43, 35, 30, 29, 32, 42, 35],
    '18-25 years': [75, 82, 86, 70, 90, 95, 86, 85, 83, 81, 96, 90, 89, 87, 93, 90, 93],
    '26-64 years': [78, 89, 89, 71, 92, 95, 91, 90, 93, 86, 92, 93, 91, 95, 95, 90, 92],
    '65+ years': [77, 80, 80, 60, 78, 76, 67, 72, 72, 76, 86, 73, 67, 69, 85, 82, 80]
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
