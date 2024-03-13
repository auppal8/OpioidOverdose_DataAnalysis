import matplotlib.pyplot as plt

#quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']
quarters = ['Q1 2022', 'Q2 2022', 'Q3 2022']

responses = {
    'Community-based self-help groups': [138, 134, 145],
    'Peer Support': [171, 160, 115],
    'Virtual check-in': [116, 106, 94],
    'Structured Cognitive Behavioral aftercare': [87, 82, 72],
    'Monitoring – Drug Testing': [55, 42, 43],
    'Unknown': [38, 34, 26]
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
ax.set_title('Stacked Bar Graph: Number of Responses by Follow-up Services')

ax.legend(bars, responses.keys())

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()