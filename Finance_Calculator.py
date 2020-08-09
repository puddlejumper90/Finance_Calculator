#Import all of the needed libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mb
import datetime
import os
import csv
import getpass
import sqlite3 as sql3

#Greeting Message
print("Welcome to your personal finance calculator! Created by puddlejumper90.")
time1 = datetime.datetime.now()
print("CURRENT TIME: ", time1)
current_time = time1
print("------------------------------------------------------------------------")

#Defined Functions

def TBL(): #Inserts two blank lines so that the application output is easier to read
    print("")
    print("")

TBL()

#Input values and variables
user = getpass.getuser()
filename = "FC_Log.csv"
database = "FC_Database.sqlite3"

#Application Processes
y_salary = float(input("Input salary, no special characters are needed: "))
TBL()
y_tax = float(input("Input expected tax rate as a decimal number (a percentage): "))
TBL()

salary_after_tax = y_salary - (y_salary * y_tax)

monthly_pay = (salary_after_tax / 12)

bi_weekly_pay = (monthly_pay / 2)

savings = float(input("Input your estimated savings rate in a decimal number (a percentage): "))
TBL()

#Additional calculations
savings_calc = float(salary_after_tax * savings)
salary_after_savings = float(salary_after_tax - savings_calc)
monthly_savings = float(savings_calc / 12)

monthly_expenses = float(input("Input your total monthly expenses as a decimal number:"))
TBL()
note = input("Please enter a note for this query: ")
left_over = float(monthly_pay - (savings + monthly_expenses))
thirty_year_savings = float(savings_calc * 30)

#Application outputs
print("----------------------------------------------------------------------------")
print("After taxes, your monthly take-home pay is: $", monthly_pay)
TBL()
print("Your left over money each month should be: $", left_over)
TBL()
print("Amount put into savings each month: $", monthly_savings)
TBL()
print("Your yearly savings should be: $", savings_calc)
TBL()
print("If you save at this rate for 30 years, you will have: $", thirty_year_savings, "If you find a way to cut your monthly costs, more money will be available for savings!")
print("Also, if you decide to invest, there is a good chance that your money will grow with the economy.")
TBL()
print("THANK YOU FOR USING THE FINANCE CALCULATOR: We are looking to add more features to this application in the near future!")

#Attribute and value lists
LIST_OF_ATTRIBUTES = ["current_time", "user", "y_salary", "y_tax", "salary_after_tax", "monthly_pay", "bi_weekly_pay", "savings", "savings_calc", "salary_after_savings", "monthly_savings", "monthly_expenses", "left_over", "note"]
LIST_OF_VALUES = [current_time, user, y_salary, y_tax, salary_after_tax, monthly_pay, bi_weekly_pay, savings, savings_calc, salary_after_savings, monthly_savings, monthly_expenses, left_over, note]
Data_Upload = [(current_time, user, y_salary, y_tax, salary_after_tax, monthly_pay, bi_weekly_pay, savings, savings_calc, salary_after_savings, monthly_savings, monthly_expenses, left_over, note)]

#More defined functions
def information():
    print("1. The purpose of this application is to provide you with enough information to make smart decisions when it comes to your finances.")
    print("2. This application keeps track of all of your inquiries so that you can analyze all of the information via spreadsheet applications.")

def add_row():
    with open("FC_Log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(LIST_OF_VALUES)
    print("The CSV file has been updated!")
        
def create_file(): #No matter what comes after this process, the csv log will already be established.
    if not os.path.isfile(filename): #This function searches the current directory for the csv file (listed above) and creates it if it does not exist
        with open (filename, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(LIST_OF_ATTRIBUTES)  
            print("Created new csv file.")
            print("Moving on to next step.")

def database_create(): #Creates a database file if it does not exits
     if not os.path.isfile(database):
        conn = sql3.connect(database)
        c = conn.cursor()
        c.execute('''CREATE TABLE FC_Log
             (current_time, user, y_salary, y_tax, salary_after_tax, monthly_pay, bi_weekly_pay, savings, savings_calc, salary_after_savings, monthly_savings, monthly_expenses, left_over, note)''')
        print("SQLite3 database has been created")
        conn.commit()
        conn.close()
     else:
        print("SQL Database was found! Moving on to next step...")  

def add_SQL_Values(): #Adds new row to the established SQLite database
    conn = sql3.connect(database)
    c = conn.cursor()
    c.executemany("INSERT into FC_Log (current_time, user, y_salary, y_tax, salary_after_tax, monthly_pay, bi_weekly_pay, savings, savings_calc, salary_after_savings, monthly_savings, monthly_expenses, left_over, note) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", Data_Upload)
    conn.commit()
    conn.close()
    print("Your query has been successfully added to the SQL database!")

def help_now():
    print("Answer all of the application's questions. The results will then be saved into both a CSV file and a SQLite database. These can be located in the application's current directory.")

#Post-query application

create_file() #Create CSV file if it does not exist
TBL()
add_row() #Append CSV file
TBL()
database_create() #Create SQL database if it does not exist
TBL()
add_SQL_Values() #Adds new values to the SQL database
TBL()
print("This query has been logged. No further action is required.")
