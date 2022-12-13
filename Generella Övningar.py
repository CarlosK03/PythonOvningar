#P7

from math import sin, cos, tan, exp, log

# def compute_functions(function, n):
#     # Create an empty list to store the results
#     result = []
    
#     # Loop through the numbers 1 through n
#     for i in range(1, n+1):
        
#         # Use eval to compute the function for the current value of i
#         result.append(eval(f'{function}({i})'))
    
#     # Return the list of results
#     return result

myF={
    "cos":cos,
    "tan":tan
}
myF1={
    "sin":sin
}
print(myF["cos"](4))

for key, Value in myF.items():
    myF1[key]=Value