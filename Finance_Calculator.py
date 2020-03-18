#Import all of the needed libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mb

#Greeting Message
print("Welcome you your personal finance calculator! :-)")

#Inserts two blank lines so that the application is easier to read for the user
def TBL():
    print("")
    print("")

TBL()

#Input values
y_salary = float(input("Input salary, no special characters are needed:"))
TBL()
y_tax = float(input("Input expected tax rate as a decimal number (a percentage):"))
TBL()

salary_after_tax = y_salary - (y_salary * y_tax)

monthly_pay = (salary_after_tax / 12)

bi_weekly_pay = (monthly_pay / 2)

savings = float(input("Input your estimated savings rate in a decimal number (a percentage):"))
TBL()

#Additional calculations
savings_calc = float(salary_after_tax * savings)
salary_after_savings = float(salary_after_tax - savings_calc)
monthly_savings = float(savings_calc / 12)

monthly_expenses = float(input("Input your total monthly expenses as a decimal number:"))
TBL()

left_over = float(monthly_pay - (savings + monthly_expenses))
thirty_year_savings = float(savings_calc * 30)

#Application outputs
print("Your left over money each month should be: $", left_over)
TBL()
print("Amount put into savings each month: $", monthly_savings)
TBL()
print("Your yearly savings should be: $", savings_calc)
TBL()
print("If you save at this rate for 30 years, you will have: $", thirty_year_savings, "If you find a way to cut your monthly costs, more money will be available for savings!")
TBL()
print("THANK YOU FOR USING THE FINANCE CALCULATOR: We are looking to add more features to this application in the near future!")