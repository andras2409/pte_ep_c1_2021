number = 13
number2 = 5 * 2
print("A number változó értéke:", number,
      "\b. Ha megszorzom kettővel, akkor", number2, "\b-t kapok.")
print("A number változó értéke: ", number,
      ". Ha megszorzom kettővel, akkor ", number2, "-t kapok.", sep = "")
print(f"A number változó értéke: {number}. Ha megszorzom kettővel, akkor {number2}-t kapok.")
print("A number változó értéke: {}. Ha megszorzom kettővel, akkor {}-t kapok.".format(number,number2))

# Igazítások
print(f"A number változó értéke: {number:<3}. Ha megszorzom kettővel, akkor {number2:>3}-t kapok.")
print("A number változó értéke: {:^3}. Ha megszorzom kettővel, akkor {:^4}-t kapok.".format(number,number2))

#Számformátumok
print(f"A number változó bináris értéke: {number:b}.")
print("A number változó oktális értéke: {:o}.".format(number))
print(f"A number változó decimális értéke: {number:d}.")
print("A number változó hexadecimális értéke: {:x} és {:X}.".format(number, number))

#Unicode karakter
number = 66
print(f"{number:c}")

#Valós számok
number = 100.1232
print(f"Tudományos: {number:e} vagy {number:E}")
print(f"valós szám: {number:f}")
print(f"3 tizedesjegy pontosság: {number:.3f}")
print(f"15 karakteren: {number:15f}")
print(f"15 karakteren, 3 tizedesjegy pontosság: {number:15.3f}")
print(f"Százalékos érték: {number:%}")
print(f"3 tizedesjegy pontosság: {number:.3%}")
print(f"15 karakteren: {number:15%}")
print(f"15 karakteren, 3 tizedesjegy pontosság: {number:15.3%}")