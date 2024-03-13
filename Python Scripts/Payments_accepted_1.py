import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019']
cash_self_payment = [86, 81, 76, 61, 78]
ahcccs = [50, 74, 80, 61, 75]
medicare = [29, 42, 42, 30, 34]
military_insurance = [29, 34, 35, 27, 31]
private_insurance = [58, 62, 65, 47, 62]
access_to_recovery = [2, 4, 2, 3, 2]
ihs_638_contract_care = [8, 11, 15, 11, 8]
medicaid = [38, 0, 0, 0, 0]
capitated = [5, 9, 5, 7, 2]
fee_for_service = [31, 50, 49, 39, 49]
sliding_fee_scale = [22, 26, 31, 28, 34]
no_fee = [4, 5, 5, 8, 5]
adc_pretrial_ddd_asi = [0, 0, 0, 0, 0]
sabg_mhgb = [0, 0, 0, 0, 0]

# Create a DataFrame
data = pd.DataFrame({
    'quarters': quarters,
    'Cash/Self Payment': cash_self_payment,
    'AHCCCS': ahcccs,
    'Medicare': medicare,
    'Military Insurance': military_insurance,
    'Private Insurance': private_insurance,
    'Access to Recovery': access_to_recovery,
    'IHS 638 Contract Care': ihs_638_contract_care,
    'Medicaid': medicaid,
    'Capitated': capitated,
    'Fee for Service': fee_for_service,
    'Sliding Fee Scale': sliding_fee_scale,
    'No Fee': no_fee,
    'ADC Pretrial DDD ASI': adc_pretrial_ddd_asi,
    'SABG MHGB': sabg_mhgb
})

colors = ['steelblue', 'lightblue', 'mediumaquamarine', 'darkorange', 'gold', 'mediumvioletred', 'maroon',
          'forestgreen', 'sienna', 'purple', 'darkseagreen', 'lightgray', 'darkblue', 'salmon']

# Set up the figure and axis
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(13, 13))
axes = axes.flatten()

# Plot donut chart for each quarter
for i, quarter in enumerate(quarters):
    quarter_data = data.loc[data['quarters'] == quarter].drop(columns='quarters').squeeze()
    if i == 0:
        wedges, text = axes[1].pie(quarter_data, colors=colors, startangle=90, wedgeprops={'width': 0.4})
        axes[1].set_title(quarter)
        axes[0].legend(wedges, quarter_data.index, loc='center')
    else:
        wedges, text = axes[i + 1].pie(quarter_data, colors=colors, startangle=90, wedgeprops={'width': 0.4})
        axes[i + 1].set_title(quarter)

    # Add value labels
    value_label = {
        'Cash/Self Payment': [330, 255, 214, 208, 139],
        'AHCCCS': [191, 231, 226, 209, 134],
        'Medicare': [113, 131, 119, 101, 60],
        'Military Insurance': [111, 107, 99, 92, 56],
        'Private Insurance': [224, 195, 184, 162, 111],
        'Access to Recovery': [6, 12, 5, 10, 3],
        'IHS 638 Contract Care': [31, 33, 42, 36, 14],
        'Medicaid': [147, 0, 0, 0, 0],
        'Capitated': [19, 27, 14, 23, 4],
        'Fee for Service': [118, 157, 139, 135, 88],
        'Sliding Fee Scale': [85, 83, 87, 95, 61],
        'No Fee': [17, 15, 14, 26, 9],
        'ADC Pretrial DDD ASI': [0, 0, 0, 0, 0],
        'SABG MHGB': [0, 0, 0, 0, 0]
    }
    for j, w in enumerate(wedges):
        value_label_key = quarter_data.index[j]
        value_label_text = str(value_label[value_label_key][i])
        if value_label_text != '0':
            text[j].set_text(value_label_text)
        else:
            text[j].set_text('')

axes[0].axis('off')  # Hide the empty subplot

# Create a legend for the donut chart
handles, labels = axes[1].get_legend_handles_labels()
fig.legend(handles, labels, loc='center')

# Adjust the plot layout
fig.suptitle('Proportion of Respondents Accepting Different Payment Methods\n')
plt.tight_layout()
plt.show()
