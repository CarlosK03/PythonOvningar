number = input()

def check_phonenumber(num: str):
    if len(num) != 12:
        return False
    if num[0] != "+":
        return False
    try:
        int(num[1:3])
        int(num[5:7])
        int(num[9:12])
    except ValueError:
        return False
    if num[3] != "-" or num[7] != "-":
        return False
    return True

def phone_num_to_int(num: str):
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