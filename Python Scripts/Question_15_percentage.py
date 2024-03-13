import matplotlib.pyplot as plt

# Sample data
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020', 'Q3 2020',
            'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

responses = {
    'cash_self_payment' : [86, 81, 76, 61, 78, 78, 72, 78, 76, 80, 88, 78, 74, 69, 71, 70, 76],
    'ahcccs' : [50, 74, 80, 61, 75, 77, 74, 79, 77, 67, 78, 77, 75, 83, 87, 86, 86],
    'medicare' : [29, 42, 42, 30, 34, 36, 27, 40, 33, 33, 35, 31, 24, 27, 35, 34, 35],
    'military_insurance' : [29, 34, 35, 27, 31, 28, 22, 30, 35, 26, 30, 28, 27, 24, 30, 27, 31],
    'private_insurance' : [58, 62, 65, 47, 62, 57, 55, 59, 56, 56, 58, 57, 57, 52, 55, 53, 59],
    'access_to_recovery' : [2, 4, 2, 3, 2, 2, 2, 2, 4, 1, 2, 2, 1, 2, 1, 4, 3],
    'ihs_638_contract_care' : [8, 11, 15, 11, 8, 10, 15, 12, 17, 8, 7, 7, 6, 10, 9, 11, 9],
    #'medicaid' : [38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'capitated' : [5, 9, 5, 7, 2, 7, 1, 4, 5, 7, 7, 3, 3, 4, 7, 7, 3],
    'fee_for_service' : [31, 50, 49, 39, 49, 55, 47, 51, 52, 38, 39, 46, 36, 39, 42, 47, 43],
    'sliding_fee_scale' : [22, 26, 31, 28, 34, 34, 25, 31, 26, 23, 37, 27, 21, 26, 28, 29, 36],
    'no_fee' : [4, 5, 5, 8, 5, 8, 5, 6, 9, 9, 9, 5, 6, 6, 8, 6, 9],
    #'adc_pretrial_ddd_asi' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 7],
    #'sabg_mhgb' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 22, 20]
}

# Plotting the line graph
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed
for response_type in responses:
    plt.plot(quarters, responses[response_type], label=response_type)

plt.xlabel('Quarters')
plt.ylabel('Percentage')
plt.title('Line Graph - Percentage of Responses by Insurance Type')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()  # To avoid any labels being cut off
plt.show()
