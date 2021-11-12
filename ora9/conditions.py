"""number = 350
if number > 100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100.")

if number % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")

number1 = 36
number2 = 9
if number1 % number2 == 0:
    print("Az első szám osztható a másodikkal")
else:
    print("Az első szám nem osztható a másodikkal")

if number1 % number2 == 2:
    print("Az első szám osztható a másodikkal")
elif number2 % number1 == 0:
    print("A második szám osztható az elsővel")
else:
    print("A számok nem oszthatóak egymással")

str4 = "radar"
if str4[0] == str4[-1]:
    print("Az első és az utolsó betű megegyezik")
else:
    print("Az első és az utolsó  betű nem egyezik meg")

a = -1
if a > 0:
    print("A szám pozitív")
elif a < 0:
    print("A szám negatív")
else:
    print("A szám nulla")

a = 1367
b = 69
c = 666
if a >= b and a >=c:
    print("Az a valtozo a legnagyobb")
    if(b>=c):
        print("A c változó a legkisebb")
    else:
        print("A b változó a legkisebb")
else:
    if b>=c:
        print("A b változó a legnagyobb")
        if a>c:
            print("A c valtozo a legkisebb")
        else:
            print("Az a valtozo a legkisebb")
    else:
        print("A c változó a legnagyobb")
        if a>b:
            print("A b valtozo a legkisebb")
        else:
            print("Az a valtozo a legkisebb")

a = 3
if a >= 3 and a < 17:
    print("Beleesik az intervallumba")
else:
    print("Nem esik bele az intervallumba")

a = 3
b = 4
c = 10
if a+b>c and a+c>b and b+c>a:
    print("A háromszög megszerkeszthető")
else:
    print("A háromszög nem megszerkeszthető")

try:
    jegy = int(input())
    if jegy == 5:
        print("Jeles")
    elif jegy == 4:
        print("Jó")
    elif jegy == 3:
        print("Közepes")
    elif jegy == 2:
        print("Elégséges")
    elif jegy == 1:
        print("Elégtelen")
    else:
        print("Hibás érték")
except ValueError:
    print("Nem számjegyekből állt a bemenet")

try:
    print(type(float(input("Kérek egy valós számot: "))))
except ValueError:
    print("Hibás bemenet")

print(type(str(7)))
print(type(str(-91.34)))
"""
try:
    szam = input()
    szam = float(szam)
    print(szam*3)
except ValueError:
    print("Nem szám")

try:
    print("Adjon meg egy egész számot")
    szam = float(input())
    print(type(szam))
    print(szam*3)
except ValueError:
    print("nem számot adott meg")





