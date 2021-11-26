import random


def maximum_keresés(lista: list[float]) -> float:
    """
    Megkeresi egy valós számokat tartalmazó lista legnagyobb elemét.
    :param lista: Valós számok listája
    :return: Valás számok maximum értéke
    """
    max = lista[0]
    for number in lista:
        if max < number:
            max = number
    return max


def kiiratas(szam: float) -> None:
    print(szam)


numbers = []
for i in range(20):
    numbers.append(random.randint(1,101))
print(numbers)

maximum = maximum_keresés(numbers)
print(maximum)
print(kiiratas(maximum))

print(maximum_keresés(numbers))