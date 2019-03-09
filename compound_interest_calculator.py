""" compound_interest_calculator.py
Calculates the interest accrued on a base amount over a given period.
Takes the AER, compounding periods and duration.
"""

def main():
    print("Enter the base amount, the annual interest (AER), the number of compounding periods, and the number of years:\n")
    currency = input("Currency (e.g. £, $ or €): ") or "€"
    principal = eval(input("Base amount (" + str(currency) + "): "))
    aer = eval(input("Annual interest rate: "))
    calculation_period = eval(input("Calculation period (years): "))
    compound_interval = input("Compound interval (yearly, half-yearly, quarterly, monthly, daily): ") or "yearly"
    regular_monthly = input("Regular monthly (- for withdraw): ") or 0

    if compound_interval == "daily":
        compound_interval_value = 365
    elif compound_interval == "monthly":
        compound_interval_value =  12
    elif compound_interval == "quarterly":
        compound_interval_value =  4
    elif compound_interval == "half-yearly":
        compound_interval_value =  2
    else:
        compound_interval_value = 1

    print("\nYear   Principal")
    print("-----------------")
    for year in range(1, calculation_period+1):
        for period in range (1, compound_interval_value+1):
            principal = principal * (1+aer/compound_interval_value/100)
            # print("Month {}".format(period))
        print("{0}        {1:.2f}".format(year, principal))

main()


