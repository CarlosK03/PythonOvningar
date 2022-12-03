#13-35 carlos
# def creates_table(n: int) -> None:
#     """
#     > This function creates a table with the name `table_<n^2>.txt` and writes the text `This is the
#     number <n^2>` to it
#     """
#     with open(f"table_{n**2}.txt", "w") as f:
#         f.write(f"This is the number {n**2}")


# def reads_table(n: int) -> None:
#     """
#     It reads the last word of the first line of a table
#     """
#     with open(f"table_{n**2}.txt", "r") as f:
#         context = f.readline().split()[-1]
#         print(f"{f.name}: {context}")


# # A way to run the code in the table.
# if __name__ == '__main__':
#     for number in range(1, 10 + 1):
#         creates_table(number)
#         reads_table(number)

#38-55 Josefines lösning
# n=int(input("number:"))
# m=int(input("number:"))
# with open(f"table_{n}.txt","w") as f, open(f"table_{m}.txt","w") as f2:
#     for i in range(1,11):
#         f.write(str(f"{n*i}"))
#         f2.write(str(f"{m*i}"))
    
# with open(f"table_{n}.txt","r") as f, open(f"table_{m}.txt","r") as f2:
#     rad= f.readline()
#     rad2=f2.readline()
#     print(rad + "\n" + rad2)
#     rad = rad.split()
#     rad2 = rad2.split()

# Dividing the numbers in the list rad and rad2 and printing them out.
# for i,j in zip(rad,rad2):
#     div=float(i)/float(j)
#     rundad=round(div, 2)
#     print(f"{i} / {j} = {rundad}",end=" ")

def individualizing_file_n(number_n: int) -> None:
    """
    It takes a number n, and writes a multiplication table for n to a table named table_n.txt
    
    Here's a one sentence summary of the above function: It takes a number, and writes a multiplication
    table for that number to a file
    
    Here's a one sentence summary of the above function: It takes two numbers, opens two files, reads
    the numbers from the files, and prints the quotients of the numbers
     
    
    Enter a number between 1-9: 3
    Enter a number between 1-9: 4
    3 / 4 = 0.75
    3 / 8 = 0.38
    3 / 12 = 0.25
    3 / 16 = 0.19
    3 / 20 = 0.15
    3 / 24 = 0.13
    3 / 28 = 0.11
    3 / 32 = 0.09
    3 / 36 = 0.08
    3 / 40 = 0.08
    3 / 44 = 0.07
    
    :param number_n: int = number_n
    :type number_n: int
    """
    """
    It takes a number n, and writes a multiplication table for n to a table named table_n.txt
    
    :param number_n: int = number_n
    :type number_n: int
    """
    increasing_number_n: int = number_n
    with open(f"table_{increasing_number_n}.txt", "w") as f:
        f.write(f"Multiplication table for n:\n")

        for multiplicator in range(1, 10 + 1):
            print(n * multiplicator, file=f)
            increasing_number_n += n


def individualizing_file_m(number_m: int) -> None:
    """
    It takes a number, and writes a multiplication table for that number to a file
    
    :param number_m: int = number_m
    :type number_m: int
    """
    increasing_number_m: int = number_m
    with open(f"table_{increasing_number_m}.txt", "w") as f:
        f.write(f"Multiplication table for m:\n")

        for multiplicator in range(1, 10 + 1):
            print(m * multiplicator, file=f)
            increasing_number_m += m


def calculate_quotients(number_n, number_m) -> None:
    """
    It takes two numbers, opens two files, reads the numbers from the files, and prints the quotients of
    the numbers
    
    :param number_n: The number of the file to read from
    :param number_m: The number of the file to divide by
    """
    with open(f"table_{number_n}.txt") as f_n, open(f"file_{number_m}.txt") as f_m:
        file_n = list(map(int, f_n.readlines()[1:]))
        file_m = list(map(int, f_m.readlines()[1:]))

        for file_number_n in file_n:
            for file_number_m in file_m:
                quotient = f"{file_number_n / file_number_m:.2f}"

                print(f"{file_number_n} / {file_number_m} = {quotient}")


if __name__ == '__main__':
    n = int(input("Enter a number between 1-9: "))
    m = int(input("Enter a number between 1-9: "))
    individualizing_file_n(n)
    individualizing_file_m(m)
    calculate_quotients(n, m)