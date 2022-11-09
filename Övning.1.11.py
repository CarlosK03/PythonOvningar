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
