#Copyright Caden Higgins and Spencer McDonald 2022 All rights reserved


#Objectives list
#Import Spreadsheet of at least 3000 companies and their end of the year stock prices
#Pick 500 at random and compare to the S&P 500 over the period of multiple years to see if the S&P 500

# https://www.interviewbit.com/blog/python-commands/

#this imports all of our resources for the rest of the code
import random
import os
import time
import csv

#this preps the CLI for the rest of the project                                                                                     .....it also flashes the word penis for a tenth of a second
os.system('cls'if os.name == 'nt' else 'clear')
time.sleep(1)
print("penis")
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

#and now we will attempt to open the stocks as a CSV

file = open('Stonkdata.csv')
csvdata = csv.reader('Stonkdata.csv')
header = []
header = next(csvdata)
header
rows = []
for row in csvdata:
    rows.append(row)
row
file.close
