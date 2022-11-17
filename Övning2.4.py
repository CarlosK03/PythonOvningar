number = input() # Input for number

def check_phonenumber(num: str):
    if len(num) != 12: #if length of num isn't 12 return false
        return False
    if num[0] != "+": #if first position in num isn't "+" return false
        return False
    try: # Checking if the input is a valid phone number.
        int(num[1:3])
        int(num[5:7])
        int(num[9:12])
    except ValueError: #if not then return false
        return False
    if num[3] != "-" or num[7] != "-": #if there isn't - in num return false
        return False
    return True

def phone_num_to_int(num: str):
    """
    It takes a string of the form "XXX-XXX-XXXX" and returns an integer of the form XXXXXXXXXX
    
    :param num: str
    :type num: str
    :return: The area code, the first three digits of the phone number, and the last four digits of the
    phone number.
    """
    return int(num[1:3]) * 1000000 + int(num[5:7]) * 1000 + int(num[9:12])

if check_phonenumber(number):
    print(phone_num_to_int(number))

    """
    It checks if the input is a valid phone number, and if it is, it returns the phone number as an
    integer
    
    :param num: str - the phone number to check
    :type num: str
    :return: The number of the phone number.
    """