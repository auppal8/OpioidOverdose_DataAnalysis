#Write a python code to create a group of barcharts that shows the number and the proportion of Verified Total Visits involving selected drugs per year. The y-axis should be the number and proportion of Verified Total Visits, and the x-axis should be the year. The data is given below:
# the data given below contains the year information. Under each year, we have a Verified Total Visits and the drugs involved along with their appearances in the eventsUnder each Verified Total Visits, we have the number of events involved and the percentage of events involved. The percentage of events involved is calculated by dividing the number of events involved by the Verified Total Visits. For example, in 2018, there are 3540 Verified Total Visits. Among these events, 449 events involved Fentanyl. The percentage of events involved Fentanyl is 449/3540 = 12.7%. The data is given below:
#Write a python code to create barcharts of the number of Verified Total Visits for each selected drugs across years.
#Also generate donut chart to show the percentage of Verified Total Visits involved for each drug for each year.
# use seaborn. The legends should be visible in the figure and not occlude the bar charts.
data = {
    "2020": {
        "Verified Total Visits": 22229,
        "Mohave County": {
            "Number of Visits": 590,
            #"% of county rate per 100,000 visits": 567.8
        },
        "Coconino County": {
            "Number of Visits": 101,
            #"% of county rate per 100,000 visits": 792.1
        },
        "Navajo County": {
            "Number of Visits": 157,
            #"% of county rate per 100,000 visits": 1020.2
        },
        "Apache County": {
            "Number of Visits": 87,
            #"% of county rate per 100,000 visits": 1178.5
        },
        "La Paz County": {
            "Number of Visits": 33,
            #"% of county rate per 100,000 visits": 372
        },
        "Yavapai County": {
            "Number of Visits": 711,
            #"% of county rate per 100,000 visits": 1032.3
        },
        "Gila County": {
            "Number of Visits": 178,
            #"% of county rate per 100,000 visits": 1074.6
        },
        "Yuma County": {
            "Number of Visits": 675,
            #"% of county rate per 100,000 visits": 936.3
        },
        "Maricopa County": {
            "Number of Visits": 13086,
            #"% of county rate per 100,000 visits": 925.7
        },
        "Pinal County": {
            "Number of Visits": 1365,
            #"% of county rate per 100,000 visits": 974.2
        },
        "Gramham County": {
            "Number of Visits": 93,
            #"% of county rate per 100,000 visits": 866.6
        },
        "Greenlee County": {
            "Number of Visits": 15,
            #"% of county rate per 100,000 visits": 1356.2
        },
        "Pima County": {
            "Number of Visits": 4530,
            #"% of county rate per 100,000 visits": 1274.1
        },
        "Santa Cuz County": {
            "Number of Visits": 168,
            #"% of county rate per 100,000 visits": 740.8
        },
        "Cochise County": {
            "Number of Visits": 440,
            #"% of county rate per 100,000 visits": 803
        },

    },
    "2021": {
        "Verified Total Visits": 23971,
        "Mohave County": {
            "Number of Visits": 665,
            #"% of county rate per 100,000 visits": 555.9
        },
        "Coconino County": {
            "Number of Visits": 477,
            #"% of county rate per 100,000 visits": 841.2
        },
        "Navajo County": {
            "Number of Visits": 297,
            #"% of county rate per 100,000 visits": 791.3
        },
        "Apache County": {
            "Number of Visits": 132,
            #"% of county rate per 100,000 visits": 983.8
        },
        "La Paz County": {
            "Number of Visits": 45,
            #"% of county rate per 100,000 visits": 421.7
        },
        "Yavapai County": {
            "Number of Visits": 1041,
            #"% of county rate per 100,000 visits": 898.1
        },
        "Gila County": {
            "Number of Visits": 206,
            #"% of county rate per 100,000 visits": 693
        },
        "Yuma County": {
            "Number of Visits": 532,
            #"% of county rate per 100,000 visits": 693
        },
        "Maricopa County": {
            "Number of Visits": 14060,
            #"% of county rate per 100,000 visits": 772.9
        },
        "Pinal County": {
            "Number of Visits": 1450,
            #"% of county rate per 100,000 visits": 780.3
        },
        "Gramham County": {
            "Number of Visits": 164,
            #"% of county rate per 100,000 visits": 617.7
        },
        "Greenlee County": {
            "Number of Visits": 21,
            #"% of county rate per 100,000 visits": 705.4
        },
        "Pima County": {
            "Number of Visits": 4254,
            #"% of county rate per 100,000 visits": 942.4
        },
        "Santa Cuz County": {
            "Number of Visits": 184,
            #"% of county rate per 100,000 visits": 848.4
        },
        "Cochise County": {
            "Number of Visits": 443,
            #"% of county rate per 100,000 visits": 716
        }

    },
    "2022": {
        "Verified Total Visits": 21345,
        "Mohave County": {
            "Number of Visits": 558,
            #"% of county rate per 100,000 visits": 487.7
        },
        "Coconino County": {
            "Number of Visits": 487,
            #"% of county rate per 100,000 visits": 588.2
        },
        "Navajo County": {
            "Number of Visits": 264,
            #"% of county rate per 100,000 visits": 509.9
        },
        "Apache County": {
            "Number of Visits": 112,
            #"% of county rate per 100,000 visits": 715.6
        },
        "La Paz County": {
            "Number of Visits": 50,
            #"% of county rate per 100,000 visits": 481.4
        },
        "Yavapai County": {
            "Number of Visits": 1007,
            #"% of county rate per 100,000 visits": 781.8
        },
        "Gila County": {
            "Number of Visits": 194,
            #"% of county rate per 100,000 visits": 548.2
        },
        "Yuma County": {
            "Number of Visits": 438,
            #"% of county rate per 100,000 visits": 559.3
        },
        "Maricopa County": {
            "Number of Visits": 12510,
            #"% of county rate per 100,000 visits": 684.6
        },
        "Pinal County": {
            "Number of Visits": 1234,
            #"% of county rate per 100,000 visits": 642.6
        },
        "Gramham County": {
            "Number of Visits": 147,
            #"% of county rate per 100,000 visits": 521.7
        },
        "Greenlee County": {
            "Number of Visits": 17,
            #"% of county rate per 100,000 visits": 535.6
        },
        "Pima County": {
            "Number of Visits": 3793,
            #"% of county rate per 100,000 visits": 773.4
        },
        "Santa Cuz County": {
            "Number of Visits": 137,
            #"% of county rate per 100,000 visits": 523.2
        },
        "Cochise County": {
            "Number of Visits": 397,
            #"% of county rate per 100,000 visits": 610.9
        }

    },
    "2023 till Q2": {
        "Verified Total Visits": 11025,
        "Mohave County": {
            "Number of Visits": 237,
            #"% of county rate per 100,000 visits": 511.9
        },
        "Coconino County": {
            "Number of Visits": 258,
            #"% of county rate per 100,000 visits": 609.3
        },
        "Navajo County": {
            "Number of Visits": 128,
            #"% of county rate per 100,000 visits": 479.4
        },
        "Apache County": {
            "Number of Visits": 54,
            #"% of county rate per 100,000 visits": 665.8
        },
        "La Paz County": {
            "Number of Visits": 17,
            #"% of county rate per 100,000 visits": 312.9
        },
        "Yavapai County": {
            "Number of Visits": 480,
            #"% of county rate per 100,000 visits": 667
        },
        "Gila County": {
            "Number of Visits": 103,
            #"% of county rate per 100,000 visits": 602.2
        },
        "Yuma County": {
            "Number of Visits": 178,
            #"% of county rate per 100,000 visits": 455.2
        },
        "Maricopa County": {
            "Number of Visits": 6503,
            #"% of county rate per 100,000 visits": 735
        },
        "Pinal County": {
            "Number of Visits": 714,
            #"% of county rate per 100,000 visits": 742.6
        },
        "Gramham County": {
            "Number of Visits": 78,
            #"% of county rate per 100,000 visits": 570.5
        },
        "Greenlee County": {
            "Number of Visits": 11,
            #"% of county rate per 100,000 visits": 728.5
        },
        "Pima County": {
            "Number of Visits": 2011,
            #"% of county rate per 100,000 visits": 807.6
        },
        "Santa Cuz County": {
            "Number of Visits": 85,
            #"% of county rate per 100,000 visits": 598.9
        },
        "Cochise County": {
            "Number of Visits": 168,
            #"% of county rate per 100,000 visits": 529.2
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
        if drug != "Verified Total Visits":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Visits": drug_data["Number of Visits"],
                #"% of county rate per 100,000 visits": drug_data[#"% of county rate per 100,000 visits"],
                "Total events": values["Verified Total Visits"]
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
    y = df[df['Drug'] == drug]['Number of Visits']
    ax.bar(x, y, width=bar_width, label=drug, color=colors[i])

# Add labels to the bars
for i, drug in enumerate(drugs):
    x = np.arange(total_years) + i * bar_width + i * spacing
    y = df[df['Drug'] == drug]['Number of Visits']
    for j, value in enumerate(y):
        if value != 0:  # Check if height is non-zero
            ax.annotate(f'{value}', (x[j] + bar_width / 2, value), xytext=(0, 5),
                        textcoords='offset points', ha='right', va='bottom', fontsize=8)

# Adjust the x-axis ticks and labels
ax.set_xticks(np.arange(total_years) + ((total_drugs - 1) * bar_width + (total_drugs - 1) * spacing) / 2)
ax.set_xticklabels(years)

plt.title('Number of Total Visits Across Years')
plt.xlabel('Year')
plt.ylabel('Number of Visits')
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()
