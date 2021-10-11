#Import the needed libraries that can analyze the data in a csv file
import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
import time
import datetime
import os
import sys
import tkinter as tk

#Basic application values
#The file name of the csv file
filename = 'FC_Log.csv'
analysis_log = 'FC_Log_Analysis.csv'
current_date = datetime.datetime.now()

#Basic Application Functions
class basic_func():

    def obl(): #prints one blanks line
        print("")

    def delay1(): #sleeps application for one second
        time.sleep(1)

#A list of functions to analyze date in 'filename'
class analysis():

    def file_check(): #checks to fee if 'FC_Log.csv' exists in the current directory
        if os.path.isfile(filename):
            print("File Found")
            basic_func.obl()
            print("Working...")
            return True
        else:
            print("File Not Found -- Cannot analyze data until data has been created.")
            basic_func.obl()
            return False
            quit()

    def user_counts(): #counts the number of unique records in the "user" column of the csv file
        if analysis.file_check() == True:
            df = pd.read_csv(filename)
            unique_users = df['user'].nunique()
            print("Unique Users: ", unique_users)
            basic_func.obl()
            return True

    
    def record_counts(): #counts the number of populated rows in 'filename'
        if analysis.file_check() == True:
            df = pd.read_csv(filename)
            record_counts = df.shape[0]
            print("Total Records: ", record_counts)
            basic_func.obl()
            return True

    def average_salary(): #Create a bar chart that shows the average 'salary' for each 'user' from 'filename'.
        if analysis.file_check() == True:
            df = pd.read_csv(filename)
            df['salary'] = df['salary'].str.replace(',', '')
            df['salary'] = df['salary'].astype(float)
            df['salary'] = df['salary'].astype(int)
            df.groupby('user')['salary'].mean().plot(kind='bar', title='Average Salary by User')
            plt.show()
            basic_func.obl()
            return True

#Aplication processes
analysis.file_check()
analysis.user_counts()
analysis.record_counts()
analysis.average_salary()
