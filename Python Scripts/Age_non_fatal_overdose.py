import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()


data = {
    "2018": {
            "Non-Fatal Opioid Overdose": 3603,
            "0-17": {
                "Number of Verified Non-Fatal Opioid Overdose": 139,
            },
            "18-24": {
                "Number of Verified Non-Fatal Opioid Overdose": 587,
            },
            "25-34": {
                "Number of Verified Non-Fatal Opioid Overdose": 964,
            },
            "35-44": {
                "Number of Verified Non-Fatal Opioid Overdose": 565,
            },
            "45-54": {
                "Number of Verified Non-Fatal Opioid Overdose": 448,
            },
            "55-64": {
                "Number of Verified Non-Fatal Opioid Overdose": 468,
            },
            "65+": {
                "Number of Verified Non-Fatal Opioid Overdose": 417,
            }
        },
    "2019": {
            "Non-Fatal Opioid Overdose": 3885,
            "0-17": {
                "Number of Verified Non-Fatal Opioid Overdose": 218,
            },
            "18-24": {
                "Number of Verified Non-Fatal Opioid Overdose": 777,
            },
            "25-34": {
                "Number of Verified Non-Fatal Opioid Overdose": 1063,
            },
            "35-44": {
                "Number of Verified Non-Fatal Opioid Overdose": 594,
            },
            "45-54": {
                "Number of Verified Non-Fatal Opioid Overdose": 491,
            },
            "55-64": {
                "Number of Verified Non-Fatal Opioid Overdose": 397,
            },
            "65+": {
                "Number of Verified Non-Fatal Opioid Overdose": 343,
            }
        },
    "2020": {
            "Non-Fatal Opioid Overdose": 4278,
            "0-17": {
                "Number of Verified Non-Fatal Opioid Overdose": 333,
            },
            "18-24": {
                "Number of Verified Non-Fatal Opioid Overdose": 823,
            },
            "25-34": {
                "Number of Verified Non-Fatal Opioid Overdose": 1263,
            },
            "35-44": {
                "Number of Verified Non-Fatal Opioid Overdose": 702,
            },
            "45-54": {
                "Number of Verified Non-Fatal Opioid Overdose": 437,
            },
            "55-64": {
                "Number of Verified Non-Fatal Opioid Overdose": 427,
            },
            "65+": {
                "Number of Verified Non-Fatal Opioid Overdose": 287,
            }
        },
    "2021": {
            "Non-Fatal Opioid Overdose": 3928,
            "0-17": {
                "Number of Verified Non-Fatal Opioid Overdose": 214,
            },
            "18-24": {
                "Number of Verified Non-Fatal Opioid Overdose": 679,
            },
            "25-34": {
                "Number of Verified Non-Fatal Opioid Overdose": 1207,
            },
            "35-44": {
                "Number of Verified Non-Fatal Opioid Overdose": 728,
            },
            "45-54": {
                "Number of Verified Non-Fatal Opioid Overdose": 439,
            },
            "55-64": {
                "Number of Verified Non-Fatal Opioid Overdose": 382,
            },
            "65+": {
                "Number of Verified Non-Fatal Opioid Overdose": 279,
            }
        },
    "2022": {
            "Non-Fatal Opioid Overdose": 3403,
            "0-17": {
                "Number of Verified Non-Fatal Opioid Overdose": 139,
            },
            "18-24": {
                "Number of Verified Non-Fatal Opioid Overdose": 486,
            },
            "25-34": {
                "Number of Verified Non-Fatal Opioid Overdose": 1082,
            },
            "35-44": {
                "Number of Verified Non-Fatal Opioid Overdose": 692,
            },
            "45-54": {
                "Number of Verified Non-Fatal Opioid Overdose": 380,
            },
            "55-64": {
                "Number of Verified Non-Fatal Opioid Overdose": 351,
            },
            "65+": {
                "Number of Verified Non-Fatal Opioid Overdose": 272,
            }
        },
    "2023 till Q2": {
            "Non-Fatal Opioid Overdose": 1899,
            "0-17": {
                "Number of Verified Non-Fatal Opioid Overdose": 66,
            },
            "18-24": {
                "Number of Verified Non-Fatal Opioid Overdose": 269,
            },
            "25-34": {
                "Number of Verified Non-Fatal Opioid Overdose": 616,
            },
            "35-44": {
                "Number of Verified Non-Fatal Opioid Overdose": 407,
            },
            "45-54": {
                "Number of Verified Non-Fatal Opioid Overdose": 213,
            },
            "55-64": {
                "Number of Verified Non-Fatal Opioid Overdose": 167,
            },
            "65+": {
                "Number of Verified Non-Fatal Opioid Overdose": 159,
            }
        }
}


# Set the color palette for the bar chart
colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon']






data_dict = []
for year, values in data.items():
    for drug, drug_data in values.items():
        if drug != "Non-Fatal Opioid Overdose":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Verified Non-Fatal Opioid Overdose": drug_data["Number of Verified Non-Fatal Opioid Overdose"],
                "Total events": values["Non-Fatal Opioid Overdose"]
            })
df = pd.DataFrame(data_dict)

# Bar Charts
plt.figure(figsize=(20, 10))
ax = sns.barplot(x='Year', y='Number of Verified Non-Fatal Opioid Overdose', hue='Drug', data=df)
plt.title('Number of Non-Fatal Opioid Overdose Across Years')
plt.legend(loc='best', bbox_to_anchor=(0.25, 1))
plt.ylabel('Number of Verified Non-Fatal Opioid Overdose')

# Add labels to the bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2, height),
                ha='center', va='bottom')
plt.show()
