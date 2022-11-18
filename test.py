# Opening the file "lol.txt" in read mode, reading the lines and then closing the file.
f=open("lol.txt","rt")
dikt=f.readlines()
f.close()

lista=["hej","på","dig"]

# f=open("lol.txt","w")
# f.write(lista[0]+"\n")
# f.write(lista[1]+"\n")
# f.write(lista[2]+"\n")
# f.close()

# Adding a new line to each element in the list.
# for i in range(len(lista)):
#     lista[i] = lista[i]+"\n"
# f=open("lol.txt","wt")
# f.writelines(lista)
# f.close()

