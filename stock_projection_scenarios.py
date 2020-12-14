#import the needed libraries
import numpy as np
import pandas as psql
import pandasql as psql

#Values
ticker = input("Please enter the Ticker symbol for the stock you wish to invest in? : ")

start_year = input("What year did this stock first go public? : ")

price = float(input("What is the current price per share for this stock? : "))

current_growth = float(input("As a float, please enter the percentage of growth from last year: "))

years = input("How many years do you want to project out to? : ")

one_year_growth = float((price * current_growth) + price)

total_growth = float((one_year_growth)^years)