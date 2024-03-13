import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = {
    "2018": {
        "Verified Overdose Deaths": 1116,
        "Mohave County": {
            "Number of Overdose Deaths": 24,
        },
        "Coconino County": {
            "Number of Overdose Deaths": 24,
        },
        "Navajo County": {
            "Number of Overdose Deaths": 0,
        },
        "Apache County": {
            "Number of Overdose Deaths": 0,
        },
        "La Paz County": {
            "Number of Overdose Deaths": 0,
        },
        "Yavapai County": {
            "Number of Overdose Deaths": 27,
        },
        "Gila County": {
            "Number of Overdose Deaths": 0,
        },
        "Yuma County": {
            "Number of Overdose Deaths": 0,
        },
        "Maricopa County": {
            "Number of Overdose Deaths": 776,
        },
        "Pinal County": {
            "Number of Overdose Deaths": 37,
        },
        "Gramham County": {
            "Number of Overdose Deaths": 0,
        },
        "Greenlee County": {
            "Number of Overdose Deaths": 0,
        },
        "Pima County": {
            "Number of Overdose Deaths": 175,
        },
        "Santa Cuz County": {
            "Number of Overdose Deaths": 0,
        },
        "Cochise County": {
            "Number of Overdose Deaths": 15,
        },
    },
    "2019": {
        "Verified Overdose Deaths": 1294,
        "Mohave County": {
            "Number of Overdose Deaths": 32,
        },
        "Coconino County": {
            "Number of Overdose Deaths": 11,
        },
        "Navajo County": {
            "Number of Overdose Deaths": 11,
        },
        "Apache County": {
            "Number of Overdose Deaths": 0,
        },
        "La Paz County": {
            "Number of Overdose Deaths": 0,
        },
        "Yavapai County": {
            "Number of Overdose Deaths": 51,
        },
        "Gila County": {
            "Number of Overdose Deaths": 0,
        },
        "Yuma County": {
            "Number of Overdose Deaths": 0,
        },
        "Maricopa County": {
            "Number of Overdose Deaths": 895,
        },
        "Pinal County": {
            "Number of Overdose Deaths": 51,
        },
        "Gramham County": {
            "Number of Overdose Deaths": 0,
        },
        "Greenlee County": {
            "Number of Overdose Deaths": 0,
        },
        "Pima County": {
            "Number of Overdose Deaths": 200,
        },
        "Santa Cuz County": {
            "Number of Overdose Deaths": 0,
        },
        "Cochise County": {
            "Number of Overdose Deaths": 16,
        },
    },
    "2020": {
        "Verified Overdose Deaths": 1886,
        "Mohave County": {
            "Number of Overdose Deaths": 35,
        },
        "Coconino County": {
            "Number of Overdose Deaths": 29,
        },
        "Navajo County": {
            "Number of Overdose Deaths": 21,
        },
        "Apache County": {
            "Number of Overdose Deaths": 14,
        },
        "La Paz County": {
            "Number of Overdose Deaths": 0,
        },
        "Yavapai County": {
            "Number of Overdose Deaths": 68,
        },
        "Gila County": {
            "Number of Overdose Deaths": 10,
        },
        "Yuma County": {
            "Number of Overdose Deaths": 0,
        },
        "Maricopa County": {
            "Number of Overdose Deaths": 1236,
        },
        "Pinal County": {
            "Number of Overdose Deaths": 83,
        },
        "Gramham County": {
            "Number of Overdose Deaths": 0,
        },
        "Greenlee County": {
            "Number of Overdose Deaths": 0,
        },
        "Pima County": {
            "Number of Overdose Deaths": 308,
        },
        "Santa Cuz County": {
            "Number of Overdose Deaths": 16,
        },
        "Cochise County": {
            "Number of Overdose Deaths": 29,
        },
    },
    "2021": {
        "Verified Overdose Deaths": 2015,
        "Mohave County": {
            "Number of Overdose Deaths": 43,
        },
        "Coconino County": {
            "Number of Overdose Deaths": 28,
        },
        "Navajo County": {
            "Number of Overdose Deaths": 30,
        },
        "Apache County": {
            "Number of Overdose Deaths": 19,
        },
        "La Paz County": {
            "Number of Overdose Deaths": 0,
        },
        "Yavapai County": {
            "Number of Overdose Deaths": 60,
        },
        "Gila County": {
            "Number of Overdose Deaths": 19,
        },
        "Yuma County": {
            "Number of Overdose Deaths": 15,
        },
        "Maricopa County": {
            "Number of Overdose Deaths": 1286,
        },
        "Pinal County": {
            "Number of Overdose Deaths": 101,
        },
        "Gramham County": {
            "Number of Overdose Deaths": 12,
        },
        "Greenlee County": {
            "Number of Overdose Deaths": 0,
        },
        "Pima County": {
            "Number of Overdose Deaths": 348,
        },
        "Santa Cuz County": {
            "Number of Overdose Deaths": 0,
        },
        "Cochise County": {
            "Number of Overdose Deaths": 16,
        },
    },
    "2022": {
        "Verified Overdose Deaths": 1927,
        "Mohave County": {
            "Number of Overdose Deaths": 40,
        },
        "Coconino County": {
            "Number of Overdose Deaths": 26,
        },
        "Navajo County": {
            "Number of Overdose Deaths": 30,
        },
        "Apache County": {
            "Number of Overdose Deaths": 25,
        },
        "La Paz County": {
            "Number of Overdose Deaths": 0,
        },
        "Yavapai County": {
            "Number of Overdose Deaths": 54,
        },
        "Gila County": {
            "Number of Overdose Deaths": 25,
        },
        "Yuma County": {
            "Number of Overdose Deaths": 17,
        },
        "Maricopa County": {
            "Number of Overdose Deaths": 1194,
        },
        "Pinal County": {
            "Number of Overdose Deaths": 86,
        },
        "Gramham County": {
            "Number of Overdose Deaths": 14,
        },
        "Greenlee County": {
            "Number of Overdose Deaths": 0,
        },
        "Pima County": {
            "Number of Overdose Deaths": 335,
        },
        "Santa Cuz County": {
            "Number of Overdose Deaths": 0,
        },
        "Cochise County": {
            "Number of Overdose Deaths": 29,
        },
    },
    "2023 till Q2": {
        "Verified Overdose Deaths": 683,
        "Mohave County": {
            "Number of Overdose Deaths": 17,
        },
        "Coconino County": {
            "Number of Overdose Deaths": 0,
        },
        "Navajo County": {
            "Number of Overdose Deaths": 16,
        },
        "Apache County": {
            "Number of Overdose Deaths": 15,
        },
        "La Paz County": {
            "Number of Overdose Deaths": 0,
        },
        "Yavapai County": {
            "Number of Overdose Deaths": 13,
        },
        "Gila County": {
            "Number of Overdose Deaths": 0,
        },
        "Yuma County": {
            "Number of Overdose Deaths": 0,
        },
        "Maricopa County": {
            "Number of Overdose Deaths": 403,
        },
        "Pinal County": {
            "Number of Overdose Deaths": 29,
        },
        "Gramham County": {
            "Number of Overdose Deaths": 0,
        },
        "Greenlee County": {
            "Number of Overdose Deaths": 0,
        },
        "Pima County": {
            "Number of Overdose Deaths": 141,
        },
        "Santa Cuz County": {
            "Number of Overdose Deaths": 0,
        },
        "Cochise County": {
            "Number of Overdose Deaths": 11,
        },
    },
}


colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon', 'teal']


# Create a DataFrame from the dictionary
data_dict = []
for year, values in data.items():
    for drug, drug_data in values.items():
        if drug != "Verified Overdose Deaths":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Overdose Deaths": drug_data["Number of Overdose Deaths"],
                "Total events": values["Verified Overdose Deaths"]
            })
df = pd.DataFrame(data_dict)

# Calculate the positions of the bars and labels
years = df['Year'].unique()
drugs = df['Drug'].unique()
total_years = len(years)
total_drugs = len(drugs)
bar_width = 0.7 / total_drugs
spacing = bar_width / 3

fig, ax = plt.subplots(figsize=(12, 6))

for i, drug in enumerate(drugs):
    x = np.arange(total_years) + i * bar_width + i * spacing
    y = df[df['Drug'] == drug]['Number of Overdose Deaths']
    ax.bar(x, y, width=bar_width, label=drug, color=colors[i])

# Add labels to the bars
for i, drug in enumerate(drugs):
    x = np.arange(total_years) + i * bar_width + i * spacing
    y = df[df['Drug'] == drug]['Number of Overdose Deaths']
    for j, value in enumerate(y):
        if value != 0:  # Check if height is non-zero
            ax.annotate(f'{value}', (x[j] + bar_width / 2, value), xytext=(0, 5),
                        textcoords='offset points', ha='right', va='bottom', fontsize=8)

# Adjust the x-axis ticks and labels
ax.set_xticks(np.arange(total_years) + ((total_drugs - 1) * bar_width + (total_drugs - 1) * spacing) / 2)
ax.set_xticklabels(years)

plt.title('Number of Verified Overdose Deaths Across Years')
plt.xlabel('Year')
plt.ylabel('Number of Overdose Deaths')
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()
