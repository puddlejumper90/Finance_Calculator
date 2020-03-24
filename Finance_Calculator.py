#Import all of the needed libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mb
import datetime
import os
import csv

#Greeting Message
print("Welcome you your personal finance calculator! :-)")
time1 = datetime.datetime.now()
print("CURRENT TIME:", time1)
current_time = time1
print("------------------------------------------------------------------------")

#Defined Functions

def TBL(): #Inserts two blank lines so that the application is easier to read
    print("")
    print("")

TBL()

#Input values and variables
user = x
filename = "FC_Log.csv"
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
#thirty_year_savings = float(savings_calc * 30)

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

LIST_OF_VALUES = [current_time, user, y_salary, y_tax, salary_after_tax, monthly_pay, bi_weekly_pay, savings, savings_calc, salary_after_savings, monthly_savings, monthly_expenses, left_over]
LIST_OF_ENTRIES =["current_time":current_time, "user":user, "y_salary":y_salary, "y_tax":y_tax, "salary_after_tax":salary_after_tax, "monthly_pay":monthly_pay, "bi_weekly_pay":bi_weekly_pay, "savings":savings, "savings_calc":savings_calc, "salary_after_savings":salary_after_savings, "monthly_savings":monthly_savings, "monthly_expenses":monthly_expenses, "left_over":left_over]

'''
#Search for "FC_Log.csv", create file if it does not exist, else add  "LIST_OF_VALUES" to the next open 
line
def search_and_append():
    with open("FC_Log.csv"):
        if not "FC_Log.csv":
            with open("FC_Log.csv", 'w', newline="LIST_OF_VALUES") as f:
                write_csv = csv.writer(f)

                write_csv.writerow(LIST_OF_ENTRIES)

        else with open ("FC_Log.csv", "rb") as f:
            write = write_csv(f)
            write.writerow(LIST_OF_ENTRIES)

'''
