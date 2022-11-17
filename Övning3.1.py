age = int(input('Please enter a persons age.'))

# if a person is 1 or younger
if age <= 1:
    print ("The person is an infant")
# if a person is older than 1 but younger or same as 13
elif age > 1 and age <= 13:
    print ("The person is a child")
# if a person is at least 13, but less than 20
elif age >= 13 and age < 20:
    print ("The person is a teenager")
elif  age >= 20:
    print ("The person is an adult")
else:
    print ("wrong age")