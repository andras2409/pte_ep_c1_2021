def megtalal(karakter: str, szoveg: str) -> int:
    """
    A karakter pozíciójának megkeresése.
    :param karakter: Egyetlen karakter, amit keresünk a szövegben.
    :param szoveg: A szöveg, amiben keressük a karaktert.
    :return: A karakter első előfordulása a szövegben, vagy -1, ha nincs benne.
    """
    pozicio = -1
    for i in range(len(szoveg)):
        if szoveg[i] == karakter and pozicio == -1:
            pozicio = i
    return pozicio

def megtalal2(karakter: str, szoveg: str) -> int:
    """
    A karakter pozíciójának megkeresése.
    :param karakter: Egyetlen karakter, amit keresünk a szövegben.
    :param szoveg: A szöveg, amiben keressük a karaktert.
    :return: A karakter első előfordulása a szövegben, vagy -1, ha nincs benne.
    """
    pozicio = -1
    i = 0
    while pozicio == -1 and i < len(szoveg):
        if szoveg[i] == karakter:
            pozicio = i
        i + 1
    return pozicio

def kacsanevek(prefixes = 'JKLMNOPQ', suffix = 'ack') -> None:
    nevek = []
    for kezdo_betu in prefixes:
        nevek.append(kezdo_betu + suffix)
    return nevek

def rendezes(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()
    for i in range(1,len(lista)):
        for j in range(len(lista) - i):
            if rendezett_lista[j] > rendezett_lista[j+1]:
                seged = rendezett_lista[j]
                rendezett_lista[j] = rendezett_lista[j+1]
                rendezett_lista[j+1] = seged
                print(rendezett_lista)
    return rendezett_lista

def minimum(lista: list[int], hanyadik = 0) -> int:
    return rendezes(lista)[hanyadik]

def osszeg(lista: list[int]) -> int:
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg

def atlag(lista: list[int]) -> float:
    return osszeg(lista) / len(lista)

print("1. feladat")
print(megtalal("a", "Indul a pap aludni."))
##print(megtalal2("a", "Indul a pap aludni."))
print("Indul a pap aludni.".find("a"))

print("2. feladat")
print(kacsanevek())

print("3. feladat")
lista = [42, 12, 76, 23, 51, 23, 36]
print(lista)
print(rendezes(lista))

print("4. feladat")
print(minimum(lista))
print(atlag(lista))
print(osszeg(lista))