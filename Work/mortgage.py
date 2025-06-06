# mortgage.py
#
# Exercise 1.7
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with 
Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.

"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    if months <= 12:
        principal = principal * (1 + rate/12) - payment - 1000
    else:
        principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment 
    months += 1
    print(months, principal, total_paid)

print('Total Paid ', total_paid)
print('Months ', months)