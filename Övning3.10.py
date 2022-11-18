# Asking the user to input the type of pizza they want.
# This is a while loop. It will keep asking the user to input the type of pizza they want until they
# enter Q.
first_choice = input("type of pizza: ")

while first_choice != "Q":
    if first_choice == "V":
        pass
    elif first_choice =="NV":
        pass
    else:
        print("option not known")
        
    first_choice = input("type of pizza: ")