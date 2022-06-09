#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on June 2022
# This is a program that rounds up a decimal


def Round_Up(User_Variable, Round_Number):
    # This Function Rounds Up The Decimal

    User_Variable[0] = User_Variable[0] * 10**Round_Number
    User_Variable[0] = User_Variable[0] + 0.5
    User_Variable[0] = int(User_Variable[0])
    User_Variable[0] = User_Variable[0] / 10**Round_Number


def main():
    # This Is The Main Function

    Answer_Number = []

    # Input

    Number = float(input("Enter a number with decimals: "))
    Round_Number = int(input("Enter how many decimal places to round by: "))
    Answer_Number.append(Number)
    Round_Up(Answer_Number, Round_Number)

    # Output

    print("The rounded number is: {0}".format(Answer_Number[0]))
    print("\nDone.")


if __name__ == "__main__":
    main()
