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


def main():
    n = int(input("Enter a number between 1-9: "))
    m = int(input("Enter a number between 1-9: "))
    individualizing_file_num(n, "n")
    individualizing_file_num(m, "m")
    calculate_quotients(n, m)

if __name__ == '__main__':
    main()
