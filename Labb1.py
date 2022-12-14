def individualizing_file_num(num: int, name: str) -> None:
    with open(f"table_{num}.txt", "w") as f:
        f.write(f"Multiplication table for {name}:\n")
        for mul in range(1, 10 + 1):
            f.write(str(num * mul) + "\n")


def calculate_quotients(n: int, m: int) -> None:
    with open(f"table_{n}.txt") as nfile, open(f"table_{m}.txt") as mfile:
        ntable = tuple(map(int, nfile.readlines()[1:]))
        mtable = tuple(map(int, mfile.readlines()[1:]))
        for tn in ntable:
            for tm in mtable:
                q = tn / tm
                print(f"{tn} / {tm} = {q:.2f}")


<<<<<<< HEAD
def main():
    n = int(input("Enter a number between 1-9: "))
    m = int(input("Enter a number between 1-9: "))
    individualizing_file_num(n, "n")
    individualizing_file_num(m, "m")
    calculate_quotients(n, m)

if __name__ == '__main__':
    main()
=======
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

<<<<<<< HEAD
#Carlos lösning
def individualizing_file(number: int) -> None:
    increasing_number: int = number
    with open(f"file_{increasing_number}.txt", "w") as f:
        f.write(f"Multiplication table for n")
        for _ in range(10+1):
            print(n*_, file=f)
            increasing_number += n
=======
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
>>>>>>> 9893429b62100ecfaa0c09dd232720f909747d4d

def individualizing_file_m(number: int) -> None:
    increasing_number_m: int = number
    with open(f"file_{increasing_number_m}.txt", "w") as f:
        f.write(f"Multiplication table for m\n")
        for x in range(10+1):
            print(m*x, file=f)
            increasing_number_m += m
            
def calc():
    




if __name__ == '__main__':
    n = int(input("Enter a number between 1-9: "))
    m = int(input("Enter a number between 1-9: "))
<<<<<<< HEAD
    individualizing_file(n)
    individualizing_file_m(m)
=======
    individualizing_file_n(n)
    individualizing_file_m(m)
    calculate_quotients(n, m)
>>>>>>> 9893429b62100ecfaa0c09dd232720f909747d4d
>>>>>>> ae715ae1771b35c28e0e028b015b4164acf3aa08
