import csv

LIST_OF_VALUES = ["current_time", "user", "y_salary", "y_tax", "salary_after_tax", "monthly_pay", "bi_weekly_pay", "savings", "savings_calc", "salary_after_savings", "monthly_savings", "monthly_expenses", "left_over"]

with open("FC_Log.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(LIST_OF_VALUES)
'''
This does work; however, I am working on a way for the application to search for the appropriate file in the current directory,
and add a row to it if it exists or create the appropriate file and then add a new row to the new file. More to follow!
'''
