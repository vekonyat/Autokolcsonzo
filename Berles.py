
class Berles:
    def __init__(self, id, auto, datum, ugyfel):
        self.id = id
        self.auto = auto
        self.datum = datum
        self.ugyfel = ugyfel

    def __str__(self):
        return f"ID: {self.id} Rendszám: {self.auto.rendszam} Típus: {self.auto.tipus} Dátum: {self.datum} Bérlő: {self.ugyfel.id}, {self.ugyfel.name} Ár: {self.auto.berleti_dij} Ft"
