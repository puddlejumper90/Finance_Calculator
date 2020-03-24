import csv

LIST_OF_VALUES = ["current_time", "user", "y_salary", "y_tax", "salary_after_tax", "monthly_pay", "bi_weekly_pay", "savings", "savings_calc", "salary_after_savings", "monthly_savings", "monthly_expenses", "left_over"]

with open("FC_Log.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(LIST_OF_VALUES)
