import matplotlib.pyplot as plt

quarters = ['Q3 2018', 'Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019', 'Q1 2020', 'Q2 2020',
            'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022']

# Example data for the number of responses for each category
cash_self_payment = [330, 255, 214, 208, 139, 159, 108, 166, 137, 167, 90, 137, 102, 123, 195, 176, 178]
ahcccs = [191, 231, 226, 209, 134, 157, 111, 170, 140, 139, 80, 135, 104, 148, 240, 215, 200]
medicare = [113, 131, 119, 101, 60, 73, 40, 86, 59, 68, 36, 55, 33, 48, 96, 86, 82]
military_insurance = [111, 107, 99, 92, 56, 57, 33, 65, 63, 54, 31, 49, 37, 42, 82, 68, 73]
private_insurance = [224, 195, 184, 162, 111, 117, 82, 126, 102, 117, 59, 99, 78, 92, 151, 134, 137]
access_to_recovery = [6, 12, 5, 10, 3, 3, 3, 5, 7, 2, 2, 4, 2, 3, 3, 9, 6]
ihs_638_contract_care = [31, 33, 42, 36, 14, 21, 23, 26, 31, 16, 7, 12, 8, 17, 24, 28, 21]
medicaid = [147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
capitated = [19, 27, 14, 23, 4, 14, 2, 9, 9, 14, 7, 5, 4, 8, 18, 18, 8]
fee_for_service = [118, 157, 139, 135, 88, 113, 71, 107, 94, 79, 40, 81, 50, 69, 116, 119, 101]
sliding_fee_scale = [85, 83, 87, 95, 61, 70, 37, 67, 47, 48, 38, 48, 29, 46, 78, 74, 84]
no_fee = [17, 15, 14, 26, 9, 16, 8, 12, 17, 18, 9, 9, 8, 10, 21, 16, 21]
adc_pretrial_ddd_asi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 16, 16]
sabg_mhgb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53, 55, 47]
# Creating the stacked bar graph
plt.figure(figsize=(10, 6))
plt.bar(quarters, cash_self_payment, label='Cash/Self-Payment')
plt.bar(quarters, ahcccs, bottom=cash_self_payment, label='AHCCCS')
plt.bar(quarters, medicare, bottom=[a + b for a, b in zip(cash_self_payment, ahcccs)], label='Medicare')
plt.bar(quarters, military_insurance,
        bottom=[a + b + c for a, b, c in zip(cash_self_payment, ahcccs, medicare)], label='Military insurance')
plt.bar(quarters, private_insurance,
        bottom=[a + b + c + d for a, b, c, d in zip(cash_self_payment, ahcccs, medicare, military_insurance)],
        label='Private health insurance')
plt.bar(quarters, access_to_recovery,
        bottom=[a + b + c + d + e for a, b, c, d, e in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance)],
        label='Access to Recovery (ATR) voucher')
plt.bar(quarters, ihs_638_contract_care,
        bottom=[a + b + c + d + e + f for a, b, c, d, e, f in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery)], label='IHS/638 contract care funds')
plt.bar(quarters, medicaid,
        bottom=[a + b + c + d + e + f + g for a, b, c, d, e, f, g in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care)], label='Medicaid')
plt.bar(quarters, capitated,
        bottom=[a + b + c + d + e + f + g + h for a, b, c, d, e, f, g, h in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care, medicaid)], label='Capitated')
plt.bar(quarters, fee_for_service,
        bottom=[a + b + c + d + e + f + g + h + i for a, b, c, d, e, f, g, h, i in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care, medicaid, capitated)],
        label='Fee-for-service')
plt.bar(quarters, sliding_fee_scale,
        bottom=[a + b + c + d + e + f + g + h + i + j for a, b, c, d, e, f, g, h, i, j in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care, medicaid, capitated, fee_for_service)],
        label='Sliding fee scale')
plt.bar(quarters, no_fee,
        bottom=[a + b + c + d + e + f + g + h + i + j + k for a, b, c, d, e, f, g, h, i, j, k in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care, medicaid, capitated, fee_for_service,
                    sliding_fee_scale)],
        label='No Fee')
plt.bar(quarters, adc_pretrial_ddd_asi,
        bottom=[a + b + c + d + e + f + g + h + i + j + k + l for a, b, c, d, e, f, g, h, i, j, k, l in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care, medicaid, capitated, fee_for_service,
                    sliding_fee_scale, no_fee)],
        label='ADC, Pre-trial, DDD/ASI')
plt.bar(quarters, sabg_mhgb,
        bottom=[a + b + c + d + e + f + g + h + i + j + k + l + m for a, b, c, d, e, f, g, h, i, j, k, l, m in
                zip(cash_self_payment, ahcccs, medicare, military_insurance, private_insurance,
                    access_to_recovery, ihs_638_contract_care, medicaid, capitated, fee_for_service,
                    sliding_fee_scale, no_fee, adc_pretrial_ddd_asi)],
        label='SABG/MHGB')

plt.xlabel('Quarters')
plt.ylabel('Number of Responses')
plt.title('Stacked Bar Graph: Number of Responses by Insurance Type')
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()