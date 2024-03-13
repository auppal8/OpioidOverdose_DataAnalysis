import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()


data = {
    "2018": {
            "Suspected EMS Responses": 5474,
            "0-17": {
                "Number of Suspected EMS Responses": 189,
            },
            "18-24": {
                "Number of Suspected EMS Responses": 852,
            },
            "25-34": {
                "Number of Suspected EMS Responses": 1477,
            },
            "35-44": {
                "Number of Suspected EMS Responses": 929,
            },
            "45-54": {
                "Number of Suspected EMS Responses": 641,
            },
            "55-64": {
                "Number of Suspected EMS Responses": 627,
            },
            "65-74": {
                "Number of Suspected EMS Responses": 369,
            },
            "75+": {
                "Number of Suspected EMS Responses": 369,
            }
        },
    "2019": {
            "Suspected EMS Responses": 7372,
            "0-17": {
                "Number of Suspected EMS Responses": 297,
            },
            "18-24": {
                "Number of Suspected EMS Responses": 1214,
            },
            "25-34": {
                "Number of Suspected EMS Responses": 1961,
            },
            "35-44": {
                "Number of Suspected EMS Responses": 1244,
            },
            "45-54": {
                "Number of Suspected EMS Responses": 895,
            },
            "55-64": {
                "Number of Suspected EMS Responses": 750,
            },
            "65-74": {
                "Number of Suspected EMS Responses": 508,
            },
            "75+": {
                "Number of Suspected EMS Responses": 481,
            }
        },
    "2020": {
            "Suspected EMS Responses": 8529,
            "0-17": {
                "Number of Suspected EMS Responses": 408,
            },
            "18-24": {
                "Number of Suspected EMS Responses": 1491,
            },
            "25-34": {
                "Number of Suspected EMS Responses": 2330,
            },
            "35-44": {
                "Number of Suspected EMS Responses": 1507,
            },
            "45-54": {
                "Number of Suspected EMS Responses": 892,
            },
            "55-64": {
                "Number of Suspected EMS Responses": 850,
            },
            "65-74": {
                "Number of Suspected EMS Responses": 542,
            },
            "75+": {
                "Number of Suspected EMS Responses": 484,
            }
        },
    "2021": {
            "Suspected EMS Responses": 8955,
            "0-17": {
                "Number of Suspected EMS Responses": 333,
            },
            "18-24": {
                "Number of Suspected EMS Responses": 1236,
            },
            "25-34": {
                "Number of Suspected EMS Responses": 2603,
            },
            "35-44": {
                "Number of Suspected EMS Responses": 1653,
            },
            "45-54": {
                "Number of Suspected EMS Responses": 1029,
            },
            "55-64": {
                "Number of Suspected EMS Responses": 913,
            },
            "65-74": {
                "Number of Suspected EMS Responses": 604,
            },
            "75+": {
                "Number of Suspected EMS Responses": 557,
            }
        },
    "2022": {
            "Suspected EMS Responses": 10093,
            "0-17": {
                "Number of Suspected EMS Responses": 305,
            },
            "18-24": {
                "Number of Suspected EMS Responses": 1234,
            },
            "25-34": {
                "Number of Suspected EMS Responses": 3220,
            },
            "35-44": {
                "Number of Suspected EMS Responses": 2160,
            },
            "45-54": {
                "Number of Suspected EMS Responses": 1150,
            },
            "55-64": {
                "Number of Suspected EMS Responses": 918,
            },
            "65-74": {
                "Number of Suspected EMS Responses": 611,
            },
            "75+": {
                "Number of Suspected EMS Responses": 446,
            }
        },
    "2023 till Q2": {
            "Suspected EMS Responses": 4535,
            "0-17": {
                "Number of Suspected EMS Responses": 138,
            },
            "18-24": {
                "Number of Suspected EMS Responses": 532,
            },
            "25-34": {
                "Number of Suspected EMS Responses": 1454,
            },
            "35-44": {
                "Number of Suspected EMS Responses": 1024,
            },
            "45-54": {
                "Number of Suspected EMS Responses": 518,
            },
            "55-64": {
                "Number of Suspected EMS Responses": 408,
            },
            "65-74": {
                "Number of Suspected EMS Responses": 216,
            },
            "75+": {
                "Number of Suspected EMS Responses": 220,
            }
    }
}


# Set the color palette for the bar chart
colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon']






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
df = pd.DataFrame(data_dict)

# Bar Charts
plt.figure(figsize=(20, 10))
ax = sns.barplot(x='Year', y='Number of Suspected EMS Responses', hue='Drug', data=df)
plt.title('Number of Suspected EMS Responses Across Years')
plt.legend(loc='best', bbox_to_anchor=(0.25, 1))
plt.ylabel('Number of Suspected EMS Responses')

# Add labels to the bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2, height),
                ha='center', va='bottom')

plt.show()
