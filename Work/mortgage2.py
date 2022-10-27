# mortgage.py
#
# Exercise 1.7
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with 
Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.

Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.
When you run the new program, it should report a total payment of 929,965.62 over 342 months.

"""
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months = months + 1
    principal = principal + (1 + rate/12) - payment
    total_paid = total_paid + payment

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment 

    print(months, round(total_paid, 2), round(principal, 2))

print('Total Paid ', round(total_paid, 2))
print('Months ', months)

