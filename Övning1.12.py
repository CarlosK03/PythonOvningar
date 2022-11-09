oldCakes=140*0.4

def price():
    cakes = int(input("Amount of cakes: "))
    priceNew=cakes*140
    priceOld=oldCakes*cakes
    print("Cakes price:", priceNew, "if they are old:", priceOld)

price();