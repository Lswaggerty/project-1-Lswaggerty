# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/11/2024
# Description: This program calculates the fewest amount of coins given an amount in cents
print("Please enter an amount in cents less than a dollar.")
cents = int(input())
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
cents = cents % 5
pennies = cents
print("Your change will be:")
print(f"Q: {quarters}")
print(f"D: {dimes}")
print(f"N: {nickels}")
print(f"P: {pennies}")


