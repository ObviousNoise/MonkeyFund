#Caden Higgins, Ryan Riccio, and Spencer McDonald ©2022 All rights reserved


#Objectives list
#Import Spreadsheet of at least 3000 companies and their end of the year stock prices
#Pick 500 at random and compare to the S&P 500 over the period of multiple years to see if the S&P 500

#https://www.interviewbit.com/blog/python-commands/


#this imports all of our resources for the rest of the code
import random
import os
import time
from stonk_data import NASDAQStockData

def clear():
    os.system('cls'if os.name == 'nt' else 'clear')


#makes a dart fly
def draw_dart():
    for spaces in range (125, 1, -1):
        time.sleep(0.001)
        clear()
        print("|" + spaces * " " + "<")


def main():
    #printing a monkey
    # Here we need to print an ASCII monkey

    print("""
            __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. \\
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
        '._ '-=-' _.'
           '~---~'
           """)

    input("Press enter to make the monkey throw the dart")
    clear()

    
draw_dart()

if __name__ == "__main__":
    main()
