from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasszam):
        super().__init__( rendszam, tipus, berleti_dij)
        self.utasszam = utasszam

    def __str__(self):
        return f"Személyautó: {self.rendszam}, {self.tipus}, {self.berleti_dij}, {self.utasszam}"
