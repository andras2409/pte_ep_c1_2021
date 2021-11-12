my_list = [1, 2.5, "alma", False]
print("A lista hossza: ", len(my_list))
print("A len() függvény visszatérési értékének típusa: ", type(len(my_list)))

print("A 2 érték benne van-e a listában: ", 2 in my_list)
print("A 2.5 érték benne van-e a listában: ", 2 in my_list)
print("Az in operátor visszatérési értékének típusa: ", type(2 in my_list))

print("A 2.5 érték pozíciója a listában: ", my_list.index(2.5))
print("Az index metódus visszatérési értékének típusa: ", type(my_list.index(2.5)))

try:
    print("A 2 érték pozíciója a listában: ", my_list.index(2))
except ValueError:
    print("A kettes érték nincs a listában")

print("A lista 1. eleme: ", my_list[0])
print("A lista utolsó eleme: ", my_list[-1])
print("A lista utolsó eleme: ", my_list[len(my_list) - 1])
print(my_list[0:2])
print(type(my_list[0:2]))

print(my_list)
my_list[0] = -3
print(my_list)
my_list.append("körte")
print(my_list)

my_list.append([1, 2, 3])
print(my_list)

my_list.extend([1, 2, 3])
print(my_list)

my_list.insert(3, "szilva")
print(my_list)