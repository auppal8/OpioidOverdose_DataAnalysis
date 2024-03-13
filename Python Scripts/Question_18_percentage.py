import matplotlib.pyplot as plt

#quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']
quarters = ['Q1 2022', 'Q2 2022', 'Q3 2022']

responses = {
    'Community-based self-help groups': [55, 60, 72],
    'Peer Support': [69, 71, 57],
    'Virtual check-in': [47, 47, 47],
    'Structured Cognitive Behavioral aftercare': [35, 37, 36],
    'Monitoring – Drug Testing': [22, 19, 21],
    'Unknown': [15, 15, 13]
}

fig, ax = plt.subplots()

bars = []
bottom = [0] * len(quarters)

for label, data in responses.items():
    bar = ax.bar(quarters, data, bottom=bottom)
    bars.append(bar)
    bottom = [b + d for b, d in zip(bottom, data)]

ax.set_xlabel('Quarters')
ax.set_ylabel('Number of Responses')
ax.set_title('Stacked Bar Graph: Percentage of Responses by Follow-up Services')

ax.legend(bars, responses.keys())

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()