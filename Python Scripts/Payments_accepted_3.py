import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']
cash_self_payment = [88, 78, 74, 69, 71, 70, 76]
ahcccs = [78, 77, 75, 83, 87, 86, 86]
medicare = [35, 31, 24, 27, 35, 34, 35]
military_insurance = [30, 28, 27, 24, 30, 27, 31]
private_insurance = [58, 57, 57, 52, 55, 53, 59]
access_to_recovery = [2, 2, 1, 2, 1, 4, 3]
ihs_638_contract_care = [7, 7, 6, 10, 9, 11, 9]
medicaid = [0, 0, 0, 0, 0, 0, 0]
capitated = [7, 3, 3, 4, 7, 7, 3]
fee_for_service = [39, 46, 36, 39, 42, 47, 43]
sliding_fee_scale = [37, 27, 21, 26, 28, 29, 36]
no_fee = [9, 5, 6, 6, 8, 6, 9]
adc_pretrial_ddd_asi = [0, 0, 0, 0, 5, 6, 7]
sabg_mhgb = [0, 0, 0, 0, 19, 22, 20]

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
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(13, 13))
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
        'Cash/Self Payment': [90, 137, 102, 123, 195, 176, 178],
        'AHCCCS': [80, 135, 104, 148, 240, 215, 200],
        'Medicare': [36, 55, 33, 48, 96, 86, 82],
        'Military Insurance': [31, 49, 37, 42, 82, 68, 73],
        'Private Insurance': [59, 99, 78, 92, 151, 134, 137],
        'Access to Recovery': [2, 4, 2, 3, 3, 9, 6],
        'IHS 638 Contract Care': [7, 12, 8, 17, 24, 28, 21],
        'Medicaid': [0, 0, 0, 0, 0, 0, 0],
        'Capitated': [7, 5, 4, 8, 18, 18, 8],
        'Fee for Service': [40, 81, 50, 69, 116, 119, 101],
        'Sliding Fee Scale': [38, 48, 29, 46, 78, 74, 84],
        'No Fee': [9, 9, 8, 10, 21, 16, 21],
        'ADC Pretrial DDD ASI': [0, 0, 0, 0, 15, 16, 16],
        'SABG MHGB': [0, 0, 0, 0, 53, 55, 47]
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
