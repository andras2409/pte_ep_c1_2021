import random
import math

print(chr(80),chr(121), chr(116), chr(104),chr(111), chr(110), sep="")
print(ord("P"))
print(ord("a"))
print(ord("A"))
print(ord(chr(80)))
print(float("3.5"))
print(type(float("3.5")))
print(int("12"))
print(int("12", base = 16))
print(hex(18))
print(bin(18))
print(oct(18))
number = 23.325236
print(number)
print(round(number))
print(round(number, 2))
print(round(number, 0))

print(float("5"))

a, b = 2, 4
if a == 4 or b != 4:
    print("nyert")
if a == 4 or b == 4:
    print("majdnem nyert")

number = 4
if number != 2:
    print("vesztett")
elif number == 3:
    print("kis türelmet kérek")
else:
    print("nyert")

a = 5
b = 1
if a == 5 and b < 2:
    print("nyert")

sebesseg = int(input("Kérem a sebességet km/h-ban: "))
print("m/s-ban: %d" %(sebesseg*3.6) )
print("m/s-ban:", sebesseg*3.6)

list = []
paros = []
paratlan = []
for i in range(100):
    list.append(random.randint(0,100))
print(list)
for elem in list:
    if elem % 2 == 0:
        paros.append(elem)
    else:
        paratlan.append(elem)
for elem in paros:
    print(elem)
for elem in paratlan:
    print(elem)

haromszog_egyik = int(input("Kérem a háromszög egyik oldalát:"))
haromszog_masik = int(input("Kérem a háromszög másik oldalát:"))
haromszog_harmadik = int(input("Kérem a háromszög harmadik oldalát:"))
kerulet = haromszog_egyik + haromszog_masik + haromszog_harmadik
d = kerulet/2
e = d * (d - haromszog_egyik) * (d - haromszog_masik) * (d - haromszog_harmadik)
print("Kerület:", kerulet)
print("Terület:",math.sqrt(e))


input_ertekek = []
while len(input_ertekek) == 0 or input_ertekek[-1]:
    input_ertekek.append(input())
input_ertekek.remove("")
print(input_ertekek)

numbers = []
for i in range(20):
    numbers.append(random.randint(1,100))
min = numbers[0]
max = numbers[0]
for number in numbers:
    if min > number:
        min = number
    if max < number:
        max = number
print(min)
print(max)

nev = input("Név: ")
nem = input("Nem (f - férfi, n - nő): ")
if nem == "f":
    print(nev, "Úr")
elif nem == "n":
    print(nev, "Asszony")
else: print(nev)