# ---Name---
# Giovani Martins

# ----Things to know-------
# P is the starting principal, r is the annual interest rate, t is the number of years invested, and n is the frequency that interest will be compounded (I set it as 1 year since the most common rate is yearly;
# at first I wanted to leave it up to the user to choose but it got confusing for me to set it up so the rate could be monthly, weekly or daily.)

# I ran some tests and compared the results from my calculator to an actual compound interest calculator online and got the same results
# https://www.thecalculatorsite.com/finance/calculators/compoundinterestcalculator.php

# For a simple program it gave me more headache than I anticipated

# ----Things left undone-------
# I didn't write a function to reverse a list


# recursive function to calculate compound interest
def compound_interest(p0, p, r, n, t, number):

    # base case
    if number == n * t:
        return (p - p0)

    interest = p * (r / (n * 100))

    # recursive case
    return compound_interest(p0, p + interest, r, n, t, number + 1)


# prompts user with questions and grabs the numbers and passes the values in order to calculate compound interest using the compound_interest function

def calculate_user_input():

    p = float(input("Enter the principal balance = "))
    r = float(input("Enter the interest rate = "))
    t = int(input("Enter the years invested  = "))
    n = 1

    # calculate the compound interest using user input values
    ci = compound_interest(p, p, r, n, t, 0)

    # rounds the final number to one decimal and prints it
    print("Compound interest = ", round(ci, 1))


# build a triangle with the # character
def triangle(num, char):

    # base case
    if num > 0:
        triangle(num-1, char)

    # recursive
    print(char*num)


# prompt menu
def print_menu():
    print("========Please select from the following=========")
    print("[1] Calculate compound interest")
    print("[2] Print a right triangle")
    print("[3] Quit")
    print("=================================================")


# checks users input then runs the appropriate code section
def process_user_input(user_choice):

    if user_choice == '1':
        calculate_user_input()
    elif user_choice == '2':
        triangle(5, "#")
    elif user_choice == '3':
        exit(0)

# run program
def main():

    while True:
        print_menu()
        user_choice = input("Please enter the number of your selection:")
        process_user_input(user_choice)

main()
