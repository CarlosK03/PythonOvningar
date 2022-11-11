savings=float(input("Please input savings: "))

def calculate():
    """
    This function calculates the amount of money you will have in your savings account after three years
    """
    firstYear=savings*1.04
    secondYear=firstYear*1.04
    thirdYear=secondYear*1.04
    print(f"{firstYear:.2f},{secondYear:.2f},{thirdYear:.2f}")

calculate();

""" 
Simplified
amount = float(input("amount:"))
rate = 0.04
balance1 = amount *(1+rate)
print("Bal after 1 year: {}".format(round(balance1)))

balance2 = balance1 *(1+rate)
print("Bal after 2 year: {}".format(round(balance2)))

balance3 = balance2 *(1+rate)
print("Bal after 3 year: {}".format(round(balance3)))
 """
