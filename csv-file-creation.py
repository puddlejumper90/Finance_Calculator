import numpy as np
import scipy as sp
import pandas as pd
import os
import csv
from os import path

testfile = 'csv_test.csv'

def createfile():
    if not os.path.isfile(testfile):
        with open(testfile, 'wb') as f:
            writer = csv.writer(f)
            print("Created new csv file.")
    else:
        print('SYSTEM: csv file exists. Moving on to next step.')
        
createfile()