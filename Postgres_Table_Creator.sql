/*
Puddlejumper90 --- 7/2/2023 --- Establish Financial_Calculator DB creation file.
*/

--Create a Database
CREATE DATABASE financial_calculator;

CREATE TABLE personal_financial_scenarios(
    current_time TIMESTAMP, 
    user VARCHAR(100),
    y_salary MONEY, 
    y_tax FLOAT, 
    salary_after_tax MONEY, 
    monthly_pay MONEY, 
    bi_weekly_pay MONEY, 
    savings MONEY, 
    savings_calc MONEY, 
    salary_after_savings MONEY, 
    monthly_savings MONEY, 
    monthly_expenses MONEY, 
    left_over MONEY, 
    note TEXT
)
