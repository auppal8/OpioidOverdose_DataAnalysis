import matplotlib.pyplot as plt

# Sample data
quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020', 'Q3 2020',
            'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

responses = {
    'cash_self_payment' : [330, 255, 214, 208, 139, 159, 108, 166, 137, 167, 90, 137, 102, 123, 195, 176, 178],
    'ahcccs' : [191, 231, 226, 209, 134, 157, 111, 170, 140, 139, 80, 135, 104, 148, 240, 215, 200],
    'medicare' : [113, 131, 119, 101, 60, 73, 40, 86, 59, 68, 36, 55, 33, 48, 96, 86, 82],
    'military_insurance' : [111, 107, 99, 92, 56, 57, 33, 65, 63, 54, 31, 49, 37, 42, 82, 68, 73],
    'private_insurance' : [224, 195, 184, 162, 111, 117, 82, 126, 102, 117, 59, 99, 78, 92, 151, 134, 137],
    'access_to_recovery' : [6, 12, 5, 10, 3, 3, 3, 5, 7, 2, 2, 4, 2, 3, 3, 9, 6],
    'ihs_638_contract_care' : [31, 33, 42, 36, 14, 21, 23, 26, 31, 16, 7, 12, 8, 17, 24, 28, 21],
    #'medicaid' : [147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'capitated' : [19, 27, 14, 23, 4, 14, 2, 9, 9, 14, 7, 5, 4, 8, 18, 18, 8],
    'fee_for_service' : [118, 157, 139, 135, 88, 113, 71, 107, 94, 79, 40, 81, 50, 69, 116, 119, 101],
    'sliding_fee_scale' : [85, 83, 87, 95, 61, 70, 37, 67, 47, 48, 38, 48, 29, 46, 78, 74, 84],
    'no_fee' : [17, 15, 14, 26, 9, 16, 8, 12, 17, 18, 9, 9, 8, 10, 21, 16, 21],
    #'adc_pretrial_ddd_asi' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 16, 16],
    #'sabg_mhgb' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53, 55, 47]
}

# Plotting the line graph
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed
for response_type in responses:
    plt.plot(quarters, responses[response_type], label=response_type)

plt.xlabel('Quarters')
plt.ylabel('Number of Responses')
plt.title('Line Graph - Number of Responses by Insurance Type')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()  # To avoid any labels being cut off
plt.show()
