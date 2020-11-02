#Import the needed libraries
import numpy as np
import pandas as pd
import pandasql as psql
import time

#Basic application functions
class basic_func():
    
    def obl(): #prints one blank line
        print("")
        
    def delay1(): #Sleeps application for two seconds
        time.sleep(1)
        
    def rec(): #Shows extra resources
        print('Good resources for stock information include Yahoo Finance and marketbeat.com')
        
class app_process():
    
    
    def user_entries():
        yearly_income = float(input('Input needed yearly income as a decimal number: '))
        basic_func.obl()
        basic_func.delay1()
        dividend = float(input('Enter projected dividend yield as a decimal number: '))
        basic_func.obl()
        basic_func.delay1()
        company = input('Please enter the ticker symbol for the company in question: ')
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
        
#User commands
#resources = basic_func.rec()        

#Application Process Chain
app_process.user_entries()