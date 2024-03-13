import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()


data = {
    "2020": {
            "Total Visits": 22229,
            "0-17": {
                "Number of Verified Total Visits": 2778,
            },
            "18-24": {
                "Number of Verified Total Visits": 3533,
            },
            "25-34": {
                "Number of Verified Total Visits": 4750,
            },
            "35-44": {
                "Number of Verified Total Visits": 3304,
            },
            "45-54": {
                "Number of Verified Total Visits": 2524,
            },
            "55-64": {
                "Number of Verified Total Visits": 2487,
            },
            "65+": {
                "Number of Verified Total Visits": 2832,
            },
            "Unknown": {
                "Number of Verified Total Visits": 23,
            }
        },
    "2021": {
            "Total Visits": 23971,
            "0-17": {
                "Number of Verified Total Visits": 3289,
            },
            "18-24": {
                "Number of Verified Total Visits": 3660,
            },
            "25-34": {
                "Number of Verified Total Visits": 5179,
            },
            "35-44": {
                "Number of Verified Total Visits": 3699,
            },
            "45-54": {
                "Number of Verified Total Visits": 2642,
            },
            "55-64": {
                "Number of Verified Total Visits": 2397,
            },
            "65+": {
                "Number of Verified Total Visits": 3091,
            },
            "Unknown": {
                "Number of Verified Total Visits": 14,
            }
        },
    "2022": {
            "Total Visits": 21345,
            "0-17": {
                "Number of Verified Total Visits": 2901,
            },
            "18-24": {
                "Number of Verified Total Visits": 2958,
            },
            "25-34": {
                "Number of Verified Total Visits": 4870,
            },
            "35-44": {
                "Number of Verified Total Visits": 3511,
            },
            "45-54": {
                "Number of Verified Total Visits": 2213,
            },
            "55-64": {
                "Number of Verified Total Visits": 2146,
            },
            "65+": {
                "Number of Verified Total Visits": 2740,
            },
            "Unknown": {
                "Number of Verified Total Visits": 0,
            }
        },
    "2023 till Q2": {
            "Total Visits": 11025,
            "0-17": {
                "Number of Verified Total Visits": 1417,
            },
            "18-24": {
                "Number of Verified Total Visits": 1422,
            },
            "25-34": {
                "Number of Verified Total Visits": 2502,
            },
            "35-44": {
                "Number of Verified Total Visits": 1931,
            },
            "45-54": {
                "Number of Verified Total Visits": 1168,
            },
            "55-64": {
                "Number of Verified Total Visits": 1078,
            },
            "65+": {
                "Number of Verified Total Visits": 1499,
            },
            "Unknown": {
                "Number of Verified Total Visits": 0,
            }
        }
}


# Set the color palette for the bar chart
colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon']





data_dict = []
for year, values in data.items():
    for drug, drug_data in values.items():
        if drug != "Total Visits":
            data_dict.append({
                "Year": year,
                "Drug": drug,
                "Number of Verified Total Visits": drug_data["Number of Verified Total Visits"],
                "Total events": values["Total Visits"]
            })
df = pd.DataFrame(data_dict)

# Bar Charts
plt.figure(figsize=(20, 10))
ax = sns.barplot(x='Year', y='Number of Verified Total Visits', hue='Drug', data=df)
plt.title('Number of Total Visits Across Years')
plt.legend(loc='best', bbox_to_anchor=(0.25, 1))
plt.ylabel('Number of Verified Total Visits')

# Add labels to the bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2, height),
                ha='center', va='bottom')

plt.show()
