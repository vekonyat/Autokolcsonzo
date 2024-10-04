from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.berelve = False

    @abstractmethod
    def __str__(self):
        pass

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasszam):
        super().__init__( rendszam, tipus, berleti_dij)
        self.utasszam = utasszam

    def __str__(self):
        return f"Személyautó: {self.rendszam}, {self.tipus}, {self.berleti_dij}, {self.utasszam}"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, terheles):
        super().__init__(rendszam, tipus, berleti_dij)
        self.terheles = terheles

    def __str__(self):
        return f"Teherautó: {self.rendszam}, {self.tipus}, {self.berleti_dij}, {self.terheles}"

class Berles:
    def __init__(self, auto, datum, ugyfel):
        self.auto = auto
        self.datum = datum
        self.ugyfel = ugyfel

    def __str__(self):
        return f"Bérlés: {self.auto.rendszam} - {self.auto.tipus}, Dátum: {self.datum}, Ügyfél: {self.ugyfel}"

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaad(self, auto):
        self.autok.append(auto)
    def __str__(self):
        return f"{self.nev} car rent - Rent a car!"

kolcsonzo = Autokolcsonzo("Renter")

auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 5000, 5)
auto2 = Szemelyauto("ABC-124", "Honda Civic", 3000, 4)
auto3 = Teherauto("ABC-125", "Ford Transit", 8000, 10)

kolcsonzo.auto_hozzaad(auto1)
kolcsonzo.auto_hozzaad(auto2)
kolcsonzo.auto_hozzaad(auto3)

print(auto1, auto2, auto3)
print(kolcsonzo, kolcsonzo.autok)

