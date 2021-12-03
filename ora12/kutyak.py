class Kutya:
    """A kutyák osztálya."""

    def __init__(self, nev: str, fajta: str):
        self.nev = nev
        self.fajat = fajta

    def __str__(self):
        return "A {} nevű kutya {} fajtájú.".format(self.nev, self.fajat)

kutya1 = Kutya("Bodri","Kuvasz")
kutya2 = Kutya("Buksi","puli")

print(kutya1)
print(kutya2)