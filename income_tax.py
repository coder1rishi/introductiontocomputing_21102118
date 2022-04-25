gross_income=input('enter gross income')
gross_income=int(gross_income)
dependent=int(input('no. of dependent'))
standard_deduction=10000
dependent_deduction=3000
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependent)
tax_rate=20
if taxable_income >0:
    tax=(taxable_income*tax_rate)/100
    print(tax)
else:
    print('no tax')




