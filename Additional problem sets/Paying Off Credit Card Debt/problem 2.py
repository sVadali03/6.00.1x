# -*- coding: utf-8 -*-
"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay 
off a credit card balance within 12 months. We will not be dealing with a minimum monthly 
payment rate. 

Take the following floating point numbers: 
  1. the outstanding balance on the credit card 
  2. annual interest rate as a decimal 
  
Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less 
than 12) it takes to pay off the debt, and the balance (likely to be a negative number).

Monthly interest rate = Annual interest rate / 12.0 
Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum 
monthly payment 

"""
out_balance = int(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))

monthly_interest_rate = annual_interest_rate / 12
monthly_payment = 0
new_balance = out_balance
num_months = 0


while new_balance > 0:
    monthly_payment += 10
    new_balance = out_balance
    


    for num_months in range(1,13):
        new_balance -= monthly_payment
        new_balance += monthly_interest_rate * new_balance
        num_months += 1
    
    
    
print("RESULT")
print(f"Monthly payment to pay off debt in 1 year: {monthly_payment}")
print(f"Number of months needed: {num_months}")
print(f"Balance: {round(new_balance,2)}")

