from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, terheles):
        super().__init__(rendszam, tipus, berleti_dij)
        self.terheles = terheles

    def __str__(self):
        return f"Teherautó: {self.rendszam}, {self.tipus}, {self.berleti_dij}, {self.terheles}"
