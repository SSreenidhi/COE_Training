# Question:
"""Write a program, which asks for the initial balance K0 and for the interest rate. The program shall calculate the new capital K1 after one year including the interest.

Extend the program with a while-loop, so that the capital Kn after a period of n years can be calculated."""

# Expected Output (example):
# Enter initial balance: 1000
# Enter interest rate (in percentage): 5
# Enter number of years: 3
# Capital after 3 years: 1157.625

K0 = float(input("Enter initial balance: "))
rate = float(input("Enter interest rate (in percentage): "))
years = int(input("Enter number of years: "))

capital = K0
for year in range(years):
    capital += capital * (rate / 100)

print(f"Capital after {years} years: {capital}")
