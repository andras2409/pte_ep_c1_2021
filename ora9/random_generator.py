import random

print(random.randint(2,400))
print(random.random())

a = random.randint(-100,100)
print(a)
if a > 0:
    print("A szám pozitív")
elif a < 0:
    print("A szám negatív")
else:
    print("A szám nulla")

