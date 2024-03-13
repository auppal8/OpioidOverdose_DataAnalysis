import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020',
            'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

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

# Ensure the lengths of quarters and response values match for all categories
#assert all(len(quarters) == len(responses[category]) for category in responses), "Length mismatch between quarters and responses"

# Create a DataFrame from the data
df = pd.DataFrame(responses, index=quarters)

# Create a bubble plot using seaborn
sns.set(style="darkgrid")
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, markers=True, legend=False, sizes=[20, 2000])

# Set the x-axis labels
plt.xticks(range(len(quarters)), quarters, rotation=45, ha='right')

# Set the y-axis labels
plt.yticks(range(len(responses)), list(responses.keys()))

# Set the chart title and axis labels
plt.title('Bubble Graph of Percentage for Total Responses by Category')
plt.xlabel('Quarters')
plt.ylabel('Categories')

# Add a legend
legend_elements = [plt.scatter([], [], s=10 * count, label=category) for category, count in
                   zip(responses.keys(), df.values.flatten())]
plt.legend(handles=legend_elements, title='Categories', loc='best')


# Show the plot
plt.tight_layout()
plt.show()
