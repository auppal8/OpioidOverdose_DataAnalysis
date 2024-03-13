import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
quarters = ['Q4 2019', 'Q1 2020', 'Q2 2020',
            'Q3 2020', 'Q4 2020']
cash_self_payment = [78, 72, 78, 76, 80]
ahcccs = [77, 74, 79, 77, 67]
medicare = [36, 27, 40, 33, 33]
military_insurance = [28, 22, 30, 35, 26]
private_insurance = [57, 55, 59, 56, 56]
access_to_recovery = [2, 2, 2, 4, 1]
ihs_638_contract_care = [10, 15, 12, 17, 8]
medicaid = [0, 0, 0, 0, 0]
capitated = [7, 1, 4, 5, 7]
fee_for_service = [55, 47, 51, 52, 38]
sliding_fee_scale = [34, 25, 31, 26, 23]
no_fee = [8, 5, 6, 9, 9]
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
        wedges, text = axes[1].pie(quarter_data, colors = colors, startangle=90, wedgeprops={'width': 0.4})
        axes[1].set_title(quarter)
        axes[0].legend(wedges, quarter_data.index, loc='center')
    else:
        wedges, text = axes[i+1].pie(quarter_data, colors = colors, startangle=90, wedgeprops={'width': 0.4})
        axes[i+1].set_title(quarter)

    # Add value labels
    value_label = {
        'Cash/Self Payment': [159, 108, 166, 137, 167],
        'AHCCCS': [157, 111, 170, 140, 139],
        'Medicare': [73, 40, 86, 59, 68],
        'Military Insurance': [57, 33, 65, 63, 54],
        'Private Insurance': [117, 82, 126, 102, 117],
        'Access to Recovery': [3, 3, 5, 7, 2],
        'IHS 638 Contract Care': [21, 23, 26, 31, 16],
        'Medicaid': [0, 0, 0, 0, 0],
        'Capitated': [14, 2, 9, 9, 14],
        'Fee for Service': [113, 71, 107, 94, 79],
        'Sliding Fee Scale': [70, 37, 67, 47, 48],
        'No Fee': [16, 8, 12, 17, 18],
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
