# -*- coding: utf-8 -*-
"""
Minimum monthly payment = Minimum monthly payment rate x Balance 
(Minimum monthly payment gets split into interest paid and principal paid) 
Interest Paid = Annual interest rate / 12 months x Balance 
Principal paid = Minimum monthly payment – Interest paid 
Remaining balance = Balance – Principal paid

Write a program to calculate the credit card balance after one year if a person only pays the 
minimum monthly payment required by the credit card company each month.

Ask the following:
    1. the outstanding balance on the credit card 
    2. annual interest rate 
    3. minimum monthly payment rate 
    
For each month, print the minimum monthly payment, remaining balance, principle paid in the 
format shown in the test cases below. All numbers should be rounded to the nearest penny. 
Finally, print the result, which should include the total amount paid that year and the remaining 
balance. 
"""
out_balance = int(input("Enter the outstanding balance on your credit card: "))
annual_interest_paid = float(input("Enter the annual credit card interest rate as a decimal: "))
min_monthly_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))

num_months = 1
total_paid = 0
print("Month: 1")
for month in range(0,12):
    min_monthly_payment = min_monthly_rate * out_balance
    print(f"Minimum monthly payment: ${round(min_monthly_payment,3)}")
    interest_paid = annual_interest_paid/ 12 * out_balance
    principal_paid = min_monthly_payment - interest_paid
    print(f"Principle paid: ${round(principal_paid,3)}")
    rem_balance = out_balance - principal_paid
    print(f"Remaining balance: ${round(rem_balance,3)}")
  
    out_balance = rem_balance
    total_paid += min_monthly_payment
    num_months+=1
    if num_months==13:
        break
    else:
        
      print(f"Month: {num_months}")


print("RESULT")
print(f"Total amount paid: ${round(total_paid,2)}")
print(f"Remaining balance: ${round(rem_balance,2)}")
  
  