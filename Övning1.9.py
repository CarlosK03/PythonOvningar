# Asking for the yearly investment, the annual interest rate, and the number of years. Then it is
# calculating the value of the investment after the number of years.
principal = eval(input("Enter the yearly investment: "))
apr = eval(input("Enter the annual interest rate: "))
years = eval(input("Enter the number of years: "))
for i in range(years):  
    principal = principal * (1+apr)
print("The value in 12 years is: ", principal)