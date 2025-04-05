#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : April 2025
# This program checks if the inputted year is a leap year or not

import math


def main():
    # Asks for user input as a string
    print(
        "Hello, this program calculates to see if the inputted year is a leap year or not. \n"
    )
    year_as_string = input("What year is it: ")

    # Tries to convert user input into an integer
    try:
        year_as_int = int(year_as_string)

        # Checks if the year is more or equal to 0
        if year_as_int > 0:

            # Checks if its evenly divisible by 4
            if year_as_int % 4 == 0:
                if year_as_int % 100 == 0:
                    if year_as_int % 400 == 0:
                        print(year_as_int, "is a leap year")
                    else:
                        print(year_as_int, "is not a leap year")
                else:
                    print(year_as_int, "is a leap year")
            else:
                print(year_as_int, "is not a leap year")

        # If user input less than 0 runs the exception
        else:
            print(year_as_int, " is not a positive number")

    # If user input cant be converted it runs the exception
    except Exception:
        print(year_as_string, ",is an invalid input")


if __name__ == "__main__":
    main()
