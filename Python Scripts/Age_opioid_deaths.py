import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()


data = {
    "2018": {
            "Opioid Deaths": 1116,
            "0-17": {
                "Number of Verified Opioid Deaths": 16,
            },
            "18-24": {
                "Number of Verified Opioid Deaths": 169,
            },
            "25-34": {
                "Number of Verified Opioid Deaths": 287,
            },
            "35-44": {
                "Number of Verified Opioid Deaths": 232,
            },
            "45-54": {
                "Number of Verified Opioid Deaths": 182,
            },
            "55-64": {
                "Number of Verified Opioid Deaths": 158,
            },
            "65+": {
                "Number of Verified Opioid Deaths": 72,
            }
        },
    "2019": {
            "Opioid Deaths": 1294,
            "0-17": {
                "Number of Verified Opioid Deaths": 26,
            },
            "18-24": {
                "Number of Verified Opioid Deaths": 195,
            },
            "25-34": {
                "Number of Verified Opioid Deaths": 343,
            },
            "35-44": {
                "Number of Verified Opioid Deaths": 283,
            },
            "45-54": {
                "Number of Verified Opioid Deaths": 197,
            },
            "55-64": {
                "Number of Verified Opioid Deaths": 180,
            },
            "65+": {
                "Number of Verified Opioid Deaths": 70,
            }
        },
    "2020": {
            "Opioid Deaths": 1886,
            "0-17": {
                "Number of Verified Opioid Deaths": 59,
            },
            "18-24": {
                "Number of Verified Opioid Deaths": 306,
            },
            "25-34": {
                "Number of Verified Opioid Deaths": 528,
            },
            "35-44": {
                "Number of Verified Opioid Deaths": 402,
            },
            "45-54": {
                "Number of Verified Opioid Deaths": 280,
            },
            "55-64": {
                "Number of Verified Opioid Deaths": 194,
            },
            "65+": {
                "Number of Verified Opioid Deaths": 287,
            }
        },
    "2021": {
            "Opioid Deaths": 2015,
            "0-17": {
                "Number of Verified Opioid Deaths": 47,
            },
            "18-24": {
                "Number of Verified Opioid Deaths": 237,
            },
            "25-34": {
                "Number of Verified Opioid Deaths": 614,
            },
            "35-44": {
                "Number of Verified Opioid Deaths": 483,
            },
            "45-54": {
                "Number of Verified Opioid Deaths": 310,
            },
            "55-64": {
                "Number of Verified Opioid Deaths": 233,
            },
            "65+": {
                "Number of Verified Opioid Deaths": 91,
            }
        },
    "2022": {
            "Opioid Deaths": 1927,
            "0-17": {
                "Number of Verified Opioid Deaths": 33,
            },
            "18-24": {
                "Number of Verified Opioid Deaths": 155,
            },
            "25-34": {
                "Number of Verified Opioid Deaths": 535,
            },
            "35-44": {
                "Number of Verified Opioid Deaths": 505,
            },
            "45-54": {
                "Number of Verified Opioid Deaths": 334,
            },
            "55-64": {
                "Number of Verified Opioid Deaths": 272,
            },
            "65+": {
                "Number of Verified Opioid Deaths": 93,
            }
        },
    "2023 till Q2": {
            "Opioid Deaths": 683,
            "0-17": {
                "Number of Verified Opioid Deaths": 10,
            },
            "18-24": {
                "Number of Verified Opioid Deaths": 58,
            },
            "25-34": {
                "Number of Verified Opioid Deaths": 183,
            },
            "35-44": {
                "Number of Verified Opioid Deaths": 170,
            },
            "45-54": {
                "Number of Verified Opioid Deaths": 111,
            },
            "55-64": {
                "Number of Verified Opioid Deaths": 101,
            },
            "65+": {
                "Number of Verified Opioid Deaths": 50,
            }
        }
}


# Set the color palette for the bar chart
colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon']






data_dict = []
for year, values in data.items():
    for drug, drug_data in values.items():
        if drug != "Opioid Deaths":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Verified Opioid Deaths": drug_data["Number of Verified Opioid Deaths"],
                "Total events": values["Opioid Deaths"]
            })
df = pd.DataFrame(data_dict)

# Bar Charts
plt.figure(figsize=(20, 10))
ax = sns.barplot(x='Year', y='Number of Verified Opioid Deaths', hue='Drug', data=df)
plt.title('Number of Opioid Deaths Across Years')
plt.legend(loc='best', bbox_to_anchor=(0.25, 1))
plt.ylabel('Number of Verified Opioid Deaths')

# Add labels to the bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2, height),
                ha='center', va='bottom')


plt.show()
