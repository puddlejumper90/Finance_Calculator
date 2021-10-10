#Import needed libraries
import numpy as np
import pandas as pd
import pandasql as psql
import time
import os
class app_func():
    
    def main_menu():
        print('Thank you for using the financial calculator, by Puddlejumper90')
        print('')
        print('===PLEASE SELECT ON OF THE FOLLOWING OPTIONS:===')
        print('')
        print('1. Finance Calculator')
        print('2. Dividend Income Calculator')
        print('3. Help')
        print('4. Exit')
        print('')
        print('==================================================')
        #Create menu selection input options
        menu_select = str(input('Please select an option: '))
        #Create if statements for each menu option
        if menu_select == '1':
            print('You have selected the finance calculator')
            #open Finance_Calculator.py
            import Finance_Calculator
            Finance_Calculator.Finance_Calculator()
            time.sleep(1)
        elif menu_select == '2':
            print('You have selected the dividend income calculator')
            time.sleep(1)
        elif menu_select == '3':
            print('You have selected the help menu')
            print('You must make a valid selection from the menu to continue with the application')
            time.sleep(2)
            print('===OPTION EXPLANATION===')
            print('1. Finance Calculator: Allows the user to enter data to view various kinds of personal financial scenarios')
            print('2. Dividend Income Calculator: Allows the user to calculate dividend payouts for a given investment')
            print('3. Help: Displays this menu')
            print('4. Exit: Allows the user to exit this application and return to the command line')
            time.sleep(1)
            app_func.main_menu()
        elif menu_select == '4':
            print('You have selected to exit the program')
            time.sleep(1)
            exit()
        else:
            print('You have selected an invalid option')
            time.sleep(1)
            app_func.main_menu()



app_func.main_menu()
