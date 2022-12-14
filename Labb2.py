def decimal_to_binary(num: int) -> str:
    return bin(num)[2:]

def binary_to_decimal(num: str) -> int:
    return int(num, 2)


decimal_num = 30 
binary_num = decimal_to_binary(decimal_num)
print(f'{decimal_num} in binary is {binary_num}')


binary_num = '101010' 
decimal_num = binary_to_decimal(binary_num)
print(f'{binary_num} in decimal is {decimal_num}')
