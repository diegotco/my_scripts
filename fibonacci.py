import math

number = 10

list_a = [0, 1]


i = 1
while i < number:
    suma = list_a[-1] + list_a[-2]
    list_a.append(suma)
    i = i + 1
print(list_a)

mylist = list(dict.fromkeys(list_a))
print(mylist)