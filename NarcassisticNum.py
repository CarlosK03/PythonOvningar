def isNarc(number):
    myList=[5,6,9,1]
    for number in myList:
        counter=0
        for digit in str(number):
            counter+=int(digit)**len(number)
        if counter==number:
            print(number)
    else: return False
        

for number in [0,10,100,1050]:
    print(isNarc(number))
    
counter=0
found=False
while not found:
    counter+=1
    found=isNarc(number+counter) or isNarc(number-counter)

if isNarc(number+counter):
    print(number+counter)
else:
    print(number-counter)            
#len(1634)=4
#1=len(1)=1=1^1=1
#1 to 9 is narcissistic
#n => len(n)
#number == digits^len(number)+digits for last^len(number)
