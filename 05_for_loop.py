'''
List iteration using for loop
'''

ISR_TAX = 0.35

salaries = [
    12000.00,
    10000.00,
    11000.00,
    10500.00,
    9000.00,
    11200.00
]

for s in salaries:
    salary_tax = s*ISR_TAX
    #print(f'{salary_tax:.2f}')
    salary_tax = round(salary_tax)
    print(salary_tax)