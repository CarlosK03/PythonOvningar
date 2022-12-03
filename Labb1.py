#13-35 carlos
# def creates_file(n: int) -> None:
#     """
#     > This function creates a file with the name `table_<n^2>.txt` and writes the text `This is the
#     number <n^2>` to it
#     """
#     with open(f"table_{n**2}.txt", "w") as f:
#         f.write(f"This is the number {n**2}")


# def reads_file(n: int) -> None:
#     """
#     It reads the last word of the first line of a file
#     """
#     with open(f"table_{n**2}.txt", "r") as f:
#         context = f.readline().split()[-1]
#         print(f"{f.name}: {context}")


# # A way to run the code in the file.
# if __name__ == '__main__':
#     for number in range(1, 10 + 1):
#         creates_file(number)
#         reads_file(number)

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

def reads_file(n: int) -> None:
    """
    It reads the last word of the first line of a file
    
def individualizing_file(number: int) -> None:
    increasing_number: int = number
    with open(f"file_{increasing_number}.txt", "w") as f:
        f.write(f"Multiplication table for ")
        for _ in range(10):
            print(n*_, file=f)
            increasing_number += n


if __name__ == '__main__':
    n = int(input("Enter a number between 1-9: "))
    m = int(input("Enter a number between 1-9: "))
    individualizing_file(n)
    individualizing_file_m(m)