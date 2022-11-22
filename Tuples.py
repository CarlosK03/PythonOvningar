# # list=[1,2,3]
# # # for x in list:
# # #     print(x,end=" ") 
# # for i in range(len(list)):
# #     print(list[i],end=" ")

# lista1=[2,4,6,8,10]
# lista2=lista1[:]
# for i in range(len(lista1)):
#     lista2[i]=lista1[i]**2
    
# print(lista2)
# print(lista1)

# lista1=[1,2,2,3,7,6,2,7,7,7,9]
# i=0
# while i<len(lista1):
#     if lista1[i]%2 !=0:
#         del lista1[i]
#     else:
#         i=i+1
# print(lista1)

# A list comprehension. It is a way to create a list in one line.
# lista1=[1,2,2,3,7,6,2,7,7,7,9]
# lista2=[i if i%2==0 else i for i in lista1]
import random
lista1=["carlos","jakob","caroline"]
lista2=[0]*3

# Creating a list of random names from the list lista1.
for i in range(len(lista2)):
    lista2[i] = lista1[random.randint(0,len(lista2)-1)]

lista2=[]
for i in range(len(lista1)):
    s=random.randint(0,len(lista1)-1)
    lista2.append(lista1[s])
    lista1.remove(lista1[s])
print(lista2)