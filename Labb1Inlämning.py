n = int(input('Number: '))
m = int(input('Number: '))
with open(f'table_{n}.txt', 'w') as f, open(f'table_{m}.txt', 'w') as f2:
    for i in range(1, 11):
        f.write(str(f' {n*i}'))
        f2.write(str(f' {m*i}'))

with open(f'table_{n}.txt', 'r') as f, open(f'table_{m}.txt', 'r') as f2:
    rad = f.readline()
    rad2 = f2.readline()
    print(rad + '\n' + rad2)
    rad = rad.split()
    rad2 = rad2.split()

for i in rad:
    for j in rad2:
        div = float(i)/float(j)
        rundad = round(div, 2)
        print(f'{i} / {j} = {rundad}')