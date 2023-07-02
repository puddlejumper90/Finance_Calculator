import time

#Basic application functions
class basic_func():
    
    @staticmethod
    def obl(): #prints one blank line
        print("")
        
    @staticmethod
    def delay1(): #Sleeps application for two seconds
        time.sleep(1)
        
    @staticmethod
    def rec(): #Shows extra resources
        print('Good resources for stock information include Yahoo Finance and marketbeat.com')

class app_process():
    
    @staticmethod
    def validate_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a decimal number.")
                continue
                
    @staticmethod
    def validate_str_input(prompt):
        while True:
            value = input(prompt)
            if value.isalpha():
                return value.upper()
            else:
                print("Invalid input. Please enter a valid string.")
                continue
        
    @staticmethod
    def user_entries():
        yearly_income = app_process.validate_float_input('Input needed yearly income as a decimal number: ')
        basic_func.obl()
        basic_func.delay1()
        dividend = app_process.validate_float_input('Enter projected dividend yield as a decimal number: ')
        basic_func.obl()
        basic_func.delay1()
        company = app_process.validate_str_input('Please enter the ticker symbol for the company in question: ')
        basic_func.obl()
        basic_func.delay1()
        total_investment = float(yearly_income/dividend)
        t_investment = print('Your total investment will need to be: $', total_investment)
        basic_func.obl()
        basic_func.delay1()
        m_income = float(yearly_income/12)
        print('Your monthly income would be: $', m_income)
        basic_func.obl()
        basic_func.delay1()
        b_even = float(total_investment/yearly_income)
        print('It will take you', b_even, 'years to break-even on this investment.')

#Application Process Chain
app_process.user_entries()
