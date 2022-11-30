# with open('table_n.txt', 'a') as f:
#     rad = int(input('Number: '))
#     for i in range(1, 11):
#         f.write(str(rad*i))
#         f.write('\n')

# search = int(input('Number: '))
# with open('table_n.txt', 'r') as f:
#     for line in f:
#         if str(search) in line:
#             print(line)

def creates_file(n: int) -> None:
    """
    > This function creates a file with the name `table_<n^2>.txt` and writes the text `This is the
    number <n^2>` to it
    
    :param n: int
    :type n: int
    """
    with open(f"table_{n**2}.txt", "w") as f:
        f.write(f"This is the number {n**2}")


def reads_file(n: int) -> None:
    """
    It reads the last word of the first line of a file
    
    :param n: int - the number of rows and columns in the table
    :type n: int
    """
    with open(f"table_{n**2}.txt", "r") as f:
        context = f.readline().split()[-1]
        print(f"{f.name}: {context}")


# A way to run the code in the file.
if __name__ == '__main__':
    for number in range(1, 10 + 1):
        creates_file(number)
        reads_file(number)