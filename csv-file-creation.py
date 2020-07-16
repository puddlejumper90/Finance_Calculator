'''
This application is just being used as an example. The following code will search the current directory for the named csv file, and create it if it does not exist.
If the file does exist, no further action is taken.

I have decided to to seperate file creation and file appending into two seperate functions. I will be adding an example of appending a csv file at a later date.

NOTE: The following code only creates a blank csv file. Depending on your application, you will need to decide when and how you will add data to it.
'''

#Import the needed libraries
import numpy as np
import scipy as sp
import pandas as pd
import os
import csv

#Establish file name
testfile = 'csv_text.csv'

#Defined functions
def createfile():
    if not os.path.isfile(testfile): #This function searches the current directory for the csv file (listed above) and creates it if it does not exist
        with open (testfile, 'wb') as f:
            writer = csv.writer(f)
            print("Created new csv file.")
            print("Moving on to next step.")
    else:
        print('SYSTEM: csv file exists. Moving on to next step.')

#Application Processes
createfile()
