#Write a python code to create a group of barcharts that shows the number and the proportion of verified non-fatal opioid overdose events involving selected drugs per year. The y-axis should be the number and proportion of verified non-fatal opioid overdose events, and the x-axis should be the year. The data is given below:
# the data given below contains the year information. Under each year, we have a verified non-fatal opioid overdose events and the drugs involved along with their appearances in the eventsUnder each verified non-fatal opioid overdose events, we have the number of events involved and the percentage of events involved. The percentage of events involved is calculated by dividing the number of events involved by the verified non-fatal opioid overdose events. For example, in 2018, there are 3540 verified non-fatal opioid overdose events. Among these events, 449 events involved Fentanyl. The percentage of events involved Fentanyl is 449/3540 = 12.7%. The data is given below:
#Write a python code to create barcharts of the number of verified non-fatal opioid overdose events for each selected drugs across years.
#Also generate donut chart to show the percentage of verified non-fatal opioid overdose events involved for each drug for each year.
# use seaborn. The legends should be visible in the figure and not occlude the bar charts.
data = {
    "2018": {
        "Verified non-fatal opioid overdose events": 3603,
        "Mohave County": {
            "Number of Non-Fatal Overdose events involved": 144,
            #"% of county rate per 100,000 popluation": 67.6
        },
        "Coconino County": {
            "Number of Non-Fatal Overdose events involved": 54,
            #"% of county rate per 100,000 popluation": 37.1
        },
        "Navajo County": {
            "Number of Non-Fatal Overdose events involved": 60,
            #"% of county rate per 100,000 popluation": 53.2
        },
        "Apache County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "La Paz County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Non-Fatal Overdose events involved": 134,
            #"% of county rate per 100,000 popluation": 58.5
        },
        "Gila County": {
            "Number of Non-Fatal Overdose events involved": 18,
            #"% of county rate per 100,000 popluation": 32.8
        },
        "Yuma County": {
            "Number of Non-Fatal Overdose events involved": 101,
            #"% of county rate per 100,000 popluation": 44.8
        },
        "Maricopa County": {
            "Number of Non-Fatal Overdose events involved": 2385,
            #"% of county rate per 100,000 popluation": 55.5
        },
        "Pinal County": {
            "Number of Non-Fatal Overdose events involved": 222,
            #"% of county rate per 100,000 popluation": 50.4
        },
        "Gramham County": {
            "Number of Non-Fatal Overdose events involved": 28,
            #"% of county rate per 100,000 popluation": 73.4
        },
        "Greenlee County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Non-Fatal Overdose events involved": 389,
            #"% of county rate per 100,000 popluation": 37.6
        },
        "Santa Cuz County": {
            "Number of Non-Fatal Overdose events involved": 15,
            #"% of county rate per 100,000 popluation": 28.6
        },
        "Cochise County": {
            "Number of Non-Fatal Overdose events involved": 36,
            #"% of county rate per 100,000 popluation": 27.6
        },

    },
    "2019": {
        "Verified non-fatal opioid overdose events": 3885,
        "Mohave County": {
            "Number of Non-Fatal Overdose events involved": 99,
            #"% of county rate per 100,000 popluation": 45.6
        },
        "Coconino County": {
            "Number of Non-Fatal Overdose events involved": 39,
            #"% of county rate per 100,000 popluation": 26.5
        },
        "Navajo County": {
            "Number of Non-Fatal Overdose events involved": 35,
            #"% of county rate per 100,000 popluation": 31
        },
        "Apache County": {
            "Number of Non-Fatal Overdose events involved": 11,
            #"% of county rate per 100,000 popluation": 15.3
        },
        "La Paz County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Non-Fatal Overdose events involved": 82,
            #"% of county rate per 100,000 popluation": 35.3
        },
        "Gila County": {
            "Number of Non-Fatal Overdose events involved": 26,
            #"% of county rate per 100,000 popluation": 47.1
        },
        "Yuma County": {
            "Number of Non-Fatal Overdose events involved": 157,
            #"% of county rate per 100,000 popluation": 68.3
        },
        "Maricopa County": {
            "Number of Non-Fatal Overdose events involved": 2497,
            #"% of county rate per 100,000 popluation": 57.1
        },
        "Pinal County": {
            "Number of Non-Fatal Overdose events involved": 264,
            #"% of county rate per 100,000 popluation": 58
        },
        "Gramham County": {
            "Number of Non-Fatal Overdose events involved": 33,
            #"% of county rate per 100,000 popluation": 85.8
        },
        "Greenlee County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Non-Fatal Overdose events involved": 601,
            #"% of county rate per 100,000 popluation": 57.5
        },
        "Santa Cuz County": {
            "Number of Non-Fatal Overdose events involved": 16,
            #"% of county rate per 100,000 popluation": 30.1
        },
        "Cochise County": {
            "Number of Non-Fatal Overdose events involved": 24,
            #"% of county rate per 100,000 popluation": 18.3
        },

    },
    "2020": {
        "Verified non-fatal opioid overdose events": 4278,
        "Mohave County": {
            "Number of Non-Fatal Overdose events involved": 78,
            #"% of county rate per 100,000 popluation": 36.5
        },
        "Coconino County": {
            "Number of Non-Fatal Overdose events involved": 32,
            #"% of county rate per 100,000 popluation": 22
        },
        "Navajo County": {
            "Number of Non-Fatal Overdose events involved": 56,
            #"% of county rate per 100,000 popluation": 52.4
        },
        "Apache County": {
            "Number of Non-Fatal Overdose events involved": 11,
            #"% of county rate per 100,000 popluation": 16.7
        },
        "La Paz County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Non-Fatal Overdose events involved": 104,
            #"% of county rate per 100,000 popluation": 43.9
        },
        "Gila County": {
            "Number of Non-Fatal Overdose events involved": 59,
            #"% of county rate per 100,000 popluation": 110.7
        },
        "Yuma County": {
            "Number of Non-Fatal Overdose events involved": 112,
            #"% of county rate per 100,000 popluation": 54.7
        },
        "Maricopa County": {
            "Number of Non-Fatal Overdose events involved": 2693,
            #"% of county rate per 100,000 popluation": 60.7
        },
        "Pinal County": {
            "Number of Non-Fatal Overdose events involved": 373,
            #"% of county rate per 100,000 popluation": 87.1
        },
        "Gramham County": {
            "Number of Non-Fatal Overdose events involved": 47,
            #"% of county rate per 100,000 popluation": 111.3
        },
        "Greenlee County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Non-Fatal Overdose events involved": 672,
            #"% of county rate per 100,000 popluation": 64.3
        },
        "Santa Cuz County": {
            "Number of Non-Fatal Overdose events involved": 21,
            #"% of county rate per 100,000 popluation": 43.9
        },
        "Cochise County": {
            "Number of Non-Fatal Overdose events involved": 20,
            #"% of county rate per 100,000 popluation": 15.9
        },

    },
    "2021": {
        "Verified non-fatal opioid overdose events": 3928,
        "Mohave County": {
            "Number of Non-Fatal Overdose events involved": 118,
            #"% of county rate per 100,000 popluation": 54.5
        },
        "Coconino County": {
            "Number of Non-Fatal Overdose events involved": 38,
            #"% of county rate per 100,000 popluation": 25.8
        },
        "Navajo County": {
            "Number of Non-Fatal Overdose events involved": 61,
            #"% of county rate per 100,000 popluation": 56.6
        },
        "Apache County": {
            "Number of Non-Fatal Overdose events involved": 26,
            #"% of county rate per 100,000 popluation": 39.2
        },
        "La Paz County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Non-Fatal Overdose events involved": 58,
            #"% of county rate per 100,000 popluation": 24
        },
        "Gila County": {
            "Number of Non-Fatal Overdose events involved": 62,
            #"% of county rate per 100,000 popluation": 115.8
        },
        "Yuma County": {
            "Number of Non-Fatal Overdose events involved": 218,
            #"% of county rate per 100,000 popluation": 105.2
        },
        "Maricopa County": {
            "Number of Non-Fatal Overdose events involved": 2389,
            #"% of county rate per 100,000 popluation": 53
        },
        "Pinal County": {
            "Number of Non-Fatal Overdose events involved": 275,
            #"% of county rate per 100,000 popluation": 62.6
        },
        "Gramham County": {
            "Number of Non-Fatal Overdose events involved": 17,
            #"% of county rate per 100,000 popluation": 43.6
        },
        "Greenlee County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Non-Fatal Overdose events involved": 622,
            #"% of county rate per 100,000 popluation": 58.8
        },
        "Santa Cuz County": {
            "Number of Non-Fatal Overdose events involved": 23,
            #"% of county rate per 100,000 popluation": 47.5
        },
        "Cochise County": {
            "Number of Non-Fatal Overdose events involved": 17,
            #"% of county rate per 100,000 popluation": 13.4
        }

    },
    "2022": {
        "Verified non-fatal opioid overdose events": 3403,
        "Mohave County": {
            "Number of Non-Fatal Overdose events involved": 56,
            #"% of county rate per 100,000 popluation": 25.9
        },
        "Coconino County": {
            "Number of Non-Fatal Overdose events involved": 30,
            #"% of county rate per 100,000 popluation": 20.3
        },
        "Navajo County": {
            "Number of Non-Fatal Overdose events involved": 51,
            #"% of county rate per 100,000 popluation": 47.3
        },
        "Apache County": {
            "Number of Non-Fatal Overdose events involved": 19,
            #"% of county rate per 100,000 popluation": 28.6
        },
        "La Paz County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Non-Fatal Overdose events involved": 27,
            #"% of county rate per 100,000 popluation": 11.2
        },
        "Gila County": {
            "Number of Non-Fatal Overdose events involved": 28,
            #"% of county rate per 100,000 popluation": 52.3
        },
        "Yuma County": {
            "Number of Non-Fatal Overdose events involved": 102,
            #"% of county rate per 100,000 popluation": 49.2
        },
        "Maricopa County": {
            "Number of Non-Fatal Overdose events involved": 2218,
            #"% of county rate per 100,000 popluation": 49.2
        },
        "Pinal County": {
            "Number of Non-Fatal Overdose events involved": 224,
            #"% of county rate per 100,000 popluation": 51
        },
        "Gramham County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Non-Fatal Overdose events involved": 613,
            #"% of county rate per 100,000 popluation": 57.9
        },
        "Santa Cuz County": {
            "Number of Non-Fatal Overdose events involved": 15,
            #"% of county rate per 100,000 popluation": 30.9
        },
        "Cochise County": {
            "Number of Non-Fatal Overdose events involved": 13,
            #"% of county rate per 100,000 popluation": 10.3
        }

    },
    "2023 till Q2": {
        "Verified non-fatal opioid overdose events": 1899,
        "Mohave County": {
            "Number of Non-Fatal Overdose events involved": 27,
            #"% of county rate per 100,000 popluation": 12.5
        },
        "Coconino County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Navajo County": {
            "Number of Non-Fatal Overdose events involved": 18,
            #"% of county rate per 100,000 popluation": 16.7
        },
        "Apache County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "La Paz County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yavapai County": {
            "Number of Non-Fatal Overdose events involved": 14,
            #"% of county rate per 100,000 popluation": 5.8
        },
        "Gila County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Yuma County": {
            "Number of Non-Fatal Overdose events involved": 46,
            #"% of county rate per 100,000 popluation": 22.2
        },
        "Maricopa County": {
            "Number of Non-Fatal Overdose events involved": 1338,
            #"% of county rate per 100,000 popluation": 29.7
        },
        "Pinal County": {
            "Number of Non-Fatal Overdose events involved": 141,
            #"% of county rate per 100,000 popluation": 32.1
        },
        "Gramham County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Greenlee County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
        },
        "Pima County": {
            "Number of Non-Fatal Overdose events involved": 277,
            #"% of county rate per 100,000 popluation": 26.2
        },
        "Santa Cuz County": {
            "Number of Non-Fatal Overdose events involved": 10,
            #"% of county rate per 100,000 popluation": 20.6
        },
        "Cochise County": {
            "Number of Non-Fatal Overdose events involved": 0,
            #"% of county rate per 100,000 popluation": 0
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
        if drug != "Verified non-fatal opioid overdose events":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Non-Fatal Overdose events involved": drug_data["Number of Non-Fatal Overdose events involved"],
                #"% of county rate per 100,000 popluation": drug_data[#"% of county rate per 100,000 popluation"],
                "Total events": values["Verified non-fatal opioid overdose events"]
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
    y = df[df['Drug'] == drug]['Number of Non-Fatal Overdose events involved']
    ax.bar(x, y, width=bar_width, label=drug, color=colors[i])

# Add labels to the bars
for i, drug in enumerate(drugs):
    x = np.arange(total_years) + i * bar_width + i * spacing
    y = df[df['Drug'] == drug]['Number of Non-Fatal Overdose events involved']
    for j, value in enumerate(y):
        if value != 0:  # Check if height is non-zero
            ax.annotate(f'{value}', (x[j] + bar_width / 2, value), xytext=(0, 5),
                        textcoords='offset points', ha='right', va='bottom', fontsize=8)

# Adjust the x-axis ticks and labels
ax.set_xticks(np.arange(total_years) + ((total_drugs - 1) * bar_width + (total_drugs - 1) * spacing) / 2)
ax.set_xticklabels(years)

plt.title('Number of Verified non-fatal opioid overdoses Across Years')
plt.xlabel('Year')
plt.ylabel('Number of Non-Fatal Overdose events involved')
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()




