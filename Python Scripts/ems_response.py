#Write a python code to create a group of barcharts that shows the number and the proportion of Suspected EMS Responses involving selected drugs per year. The y-axis should be the number and proportion of Suspected EMS Responses, and the x-axis should be the year. The data is given below:
# the data given below contains the year information. Under each year, we have a Suspected EMS Responses and the drugs involved along with their appearances in the eventsUnder each Suspected EMS Responses, we have the number of events involved and the percentage of events involved. The percentage of events involved is calculated by dividing the number of events involved by the Suspected EMS Responses. For example, in 2018, there are 3540 Suspected EMS Responses. Among these events, 449 events involved Fentanyl. The percentage of events involved Fentanyl is 449/3540 = 12.7%. The data is given below:
#Write a python code to create barcharts of the number of Suspected EMS Responses for each selected drugs across years.
#Also generate donut chart to show the percentage of Suspected EMS Responses involved for each drug for each year.
# use seaborn. The legends should be visible in the figure and not occlude the bar charts.
data = {
    "2018": {
        "Suspected EMS Responses": 5474,
        "Mohave County": {
            "Number of Suspected EMS Responses": 155,
            #"% of county rate per 100,000 popluation": 72.8
        },
        "Coconino County": {
            "Number of Suspected EMS Responses": 36,
            #"% of county rate per 100,000 popluation": 24.7
        },
        "Navajo County": {
            "Number of Suspected EMS Responses": 85,
            #"% of county rate per 100,000 popluation": 75.4
        },
        "Apache County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "La Paz County": {
            "Number of Suspected EMS Responses": 35,
            #"% of county rate per 100,000 popluation": 159.9
        },
        "Yavapai County": {
            "Number of Suspected EMS Responses": 285,
            #"% of county rate per 100,000 popluation": 124.5
        },
        "Gila County": {
            "Number of Suspected EMS Responses": 26,
            #"% of county rate per 100,000 popluation": 47.3
        },
        "Yuma County": {
            "Number of Suspected EMS Responses": 129,
            #"% of county rate per 100,000 popluation": 57.3
        },
        "Maricopa County": {
            "Number of Suspected EMS Responses": 3323,
            #"% of county rate per 100,000 popluation": 77.4
        },
        "Pinal County": {
            "Number of Suspected EMS Responses": 241,
            #"% of county rate per 100,000 popluation": 54.7
        },
        "Gramham County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Suspected EMS Responses": 1000,
            #"% of county rate per 100,000 popluation": 96.7
        },
        "Santa Cuz County": {
            "Number of Suspected EMS Responses": 94,
            #"% of county rate per 100,000 popluation": 179.4
        },
        "Cochise County": {
            "Number of Suspected EMS Responses": 57,
            #"% of county rate per 100,000 popluation": 43.7
        },

    },
    "2019": {
        "Suspected EMS Responses": 7372,
        "Mohave County": {
            "Number of Suspected EMS Responses": 172,
            #"% of county rate per 100,000 popluation": 79.3
        },
        "Coconino County": {
            "Number of Suspected EMS Responses": 49,
            #"% of county rate per 100,000 popluation": 33.3
        },
        "Navajo County": {
            "Number of Suspected EMS Responses": 83,
            #"% of county rate per 100,000 popluation": 73.6
        },
        "Apache County": {
            "Number of Suspected EMS Responses": 32,
            #"% of county rate per 100,000 popluation": 44.6
        },
        "La Paz County": {
            "Number of Suspected EMS Responses": 34,
            #"% of county rate per 100,000 popluation": 154
        },
        "Yavapai County": {
            "Number of Suspected EMS Responses": 403,
            #"% of county rate per 100,000 popluation": 173.4
        },
        "Gila County": {
            "Number of Suspected EMS Responses": 21,
            #"% of county rate per 100,000 popluation": 38.1
        },
        "Yuma County": {
            "Number of Suspected EMS Responses": 314,
            #"% of county rate per 100,000 popluation": 136.5
        },
        "Maricopa County": {
            "Number of Suspected EMS Responses": 4347,
            #"% of county rate per 100,000 popluation": 99.5
        },
        "Pinal County": {
            "Number of Suspected EMS Responses": 304,
            #"% of county rate per 100,000 popluation": 66.8
        },
        "Gramham County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Suspected EMS Responses": 1452,
            #"% of county rate per 100,000 popluation": 139
        },
        "Santa Cuz County": {
            "Number of Suspected EMS Responses": 83,
            #"% of county rate per 100,000 popluation": 156.1
        },
        "Cochise County": {
            "Number of Suspected EMS Responses": 74,
            #"% of county rate per 100,000 popluation": 56.6
        },

    },
    "2020": {
        "Suspected EMS Responses": 8529,
        "Mohave County": {
            "Number of Suspected EMS Responses": 143,
            #"% of county rate per 100,000 popluation": 66.8
        },
        "Coconino County": {
            "Number of Suspected EMS Responses": 70,
            #"% of county rate per 100,000 popluation": 48
        },
        "Navajo County": {
            "Number of Suspected EMS Responses": 104,
            #"% of county rate per 100,000 popluation": 97.4
        },
        "Apache County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "La Paz County": {
            "Number of Suspected EMS Responses": 31,
            #"% of county rate per 100,000 popluation": 186.9
        },
        "Yavapai County": {
            "Number of Suspected EMS Responses": 488,
            #"% of county rate per 100,000 popluation": 205.8
        },
        "Gila County": {
            "Number of Suspected EMS Responses": 28,
            #"% of county rate per 100,000 popluation": 52.5
        },
        "Yuma County": {
            "Number of Suspected EMS Responses": 311,
            #"% of county rate per 100,000 popluation": 151.9
        },
        "Maricopa County": {
            "Number of Suspected EMS Responses": 4810,
            #"% of county rate per 100,000 popluation": 108.4
        },
        "Pinal County": {
            "Number of Suspected EMS Responses": 419,
            #"% of county rate per 100,000 popluation": 97.8
        },
        "Gramham County": {
            "Number of Suspected EMS Responses": 10,
            #"% of county rate per 100,000 popluation": 25.9
        },
        "Greenlee County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Suspected EMS Responses": 1903,
            #"% of county rate per 100,000 popluation": 182
        },
        "Santa Cuz County": {
            "Number of Suspected EMS Responses": 108,
            #"% of county rate per 100,000 popluation": 226
        },
        "Cochise County": {
            "Number of Suspected EMS Responses": 99,
            #"% of county rate per 100,000 popluation": 78.7
        },

    },
    "2021": {
        "Suspected EMS Responses": 8955,
        "Mohave County": {
            "Number of Suspected EMS Responses": 189,
            #"% of county rate per 100,000 popluation": 87.3
        },
        "Coconino County": {
            "Number of Suspected EMS Responses": 63,
            #"% of county rate per 100,000 popluation": 42.7
        },
        "Navajo County": {
            "Number of Suspected EMS Responses": 128,
            #"% of county rate per 100,000 popluation": 118.8
        },
        "Apache County": {
            "Number of Suspected EMS Responses": 13,
            #"% of county rate per 100,000 popluation": 19.6
        },
        "La Paz County": {
            "Number of Suspected EMS Responses": 40,
            #"% of county rate per 100,000 popluation": 237.8
        },
        "Yavapai County": {
            "Number of Suspected EMS Responses": 448,
            #"% of county rate per 100,000 popluation": 185.8
        },
        "Gila County": {
            "Number of Suspected EMS Responses": 54,
            #"% of county rate per 100,000 popluation": 100.9
        },
        "Yuma County": {
            "Number of Suspected EMS Responses": 264,
            #"% of county rate per 100,000 popluation": 127.3
        },
        "Maricopa County": {
            "Number of Suspected EMS Responses": 5287,
            #"% of county rate per 100,000 popluation": 117.3
        },
        "Pinal County": {
            "Number of Suspected EMS Responses": 374,
            #"% of county rate per 100,000 popluation": 85.2
        },
        "Gramham County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Suspected EMS Responses": 1840,
            #"% of county rate per 100,000 popluation": 173.9
        },
        "Santa Cuz County": {
            "Number of Suspected EMS Responses": 139,
            #"% of county rate per 100,000 popluation": 286.8
        },
        "Cochise County": {
            "Number of Suspected EMS Responses": 108,
            #"% of county rate per 100,000 popluation": 85.4
        }

    },
    "2022": {
        "Suspected EMS Responses": 10093,
        "Mohave County": {
            "Number of Suspected EMS Responses": 125,
            #"% of county rate per 100,000 popluation": 57.7
        },
        "Coconino County": {
            "Number of Suspected EMS Responses": 55,
            #"% of county rate per 100,000 popluation": 37.3
        },
        "Navajo County": {
            "Number of Suspected EMS Responses": 68,
            #"% of county rate per 100,000 popluation": 63.1
        },
        "Apache County": {
            "Number of Suspected EMS Responses": 18,
            #"% of county rate per 100,000 popluation": 27.1
        },
        "La Paz County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 89.2
        },
        "Yavapai County": {
            "Number of Suspected EMS Responses": 235,
            #"% of county rate per 100,000 popluation": 97.4
        },
        "Gila County": {
            "Number of Suspected EMS Responses": 24,
            #"% of county rate per 100,000 popluation": 44.8
        },
        "Yuma County": {
            "Number of Suspected EMS Responses": 196,
            #"% of county rate per 100,000 popluation": 94.5
        },
        "Maricopa County": {
            "Number of Suspected EMS Responses": 7340,
            #"% of county rate per 100,000 popluation": 162.8
        },
        "Pinal County": {
            "Number of Suspected EMS Responses": 343,
            #"% of county rate per 100,000 popluation": 78.1
        },
        "Gramham County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Suspected EMS Responses": 1470,
            #"% of county rate per 100,000 popluation": 138.9
        },
        "Santa Cuz County": {
            "Number of Suspected EMS Responses": 101,
            #"% of county rate per 100,000 popluation": 208.4
        },
        "Cochise County": {
            "Number of Suspected EMS Responses": 93,
            #"% of county rate per 100,000 popluation": 73.5
        }

    },
    "2023 till Q2": {
        "Suspected EMS Responses": 4535,
        "Mohave County": {
            "Number of Suspected EMS Responses": 54,
            #"% of county rate per 100,000 popluation": 24.9
        },
        "Coconino County": {
            "Number of Suspected EMS Responses": 26,
            #"% of county rate per 100,000 popluation": 17.6
        },
        "Navajo County": {
            "Number of Suspected EMS Responses": 39,
            #"% of county rate per 100,000 popluation": 36.2
        },
        "Apache County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "La Paz County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Suspected EMS Responses": 111,
            #"% of county rate per 100,000 popluation": 46
        },
        "Gila County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yuma County": {
            "Number of Suspected EMS Responses": 98,
            #"% of county rate per 100,000 popluation": 47.3
        },
        "Maricopa County": {
            "Number of Suspected EMS Responses": 3435,
            #"% of county rate per 100,000 popluation": 76.2
        },
        "Pinal County": {
            "Number of Suspected EMS Responses": 180,
            #"% of county rate per 100,000 popluation": 41
        },
        "Gramham County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Suspected EMS Responses": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Suspected EMS Responses": 462,
            #"% of county rate per 100,000 popluation": 43.7
        },
        "Santa Cuz County": {
            "Number of Suspected EMS Responses": 57,
            #"% of county rate per 100,000 popluation": 117.6
        },
        "Cochise County": {
            "Number of Suspected EMS Responses": 46,
            #"% of county rate per 100,000 popluation": 36.4
        }

    }
}

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Create a DataFrame from the dictionary
data_dict = []
for year, values in data.items():
    for drug, drug_data in values.items():
        if drug != "Suspected EMS Responses":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Suspected EMS Responses": drug_data["Number of Suspected EMS Responses"],
                "Total events": values["Suspected EMS Responses"]
            })
colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon', 'teal']

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
    y = df[df['Drug'] == drug]['Number of Suspected EMS Responses']
    ax.bar(x, y, width=bar_width, label=drug, color=colors[i])

# Add labels to the bars
for i, drug in enumerate(drugs):
    x = np.arange(total_years) + i * bar_width + i * spacing
    y = df[df['Drug'] == drug]['Number of Suspected EMS Responses']
    for j, value in enumerate(y):
        if value != 0:  # Check if height is non-zero
            ax.annotate(f'{value}', (x[j] + bar_width / 2, value), xytext=(0, 5),
                        textcoords='offset points', ha='right', va='bottom', fontsize=8)

# Adjust the x-axis ticks and labels
ax.set_xticks(np.arange(total_years) + ((total_drugs - 1) * bar_width + (total_drugs - 1) * spacing) / 2)
ax.set_xticklabels(years)

plt.title('Number of Total Suspected EMS Responses Across Years')
plt.xlabel('Year')
plt.ylabel('Number of Suspected EMS Responses')
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()

