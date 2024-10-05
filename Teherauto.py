from Auto import Auto

class Teherauto(Auto):
    def __init__(self, id, rendszam, tipus, berleti_dij, terheles):
        super().__init__(id, rendszam, tipus, berleti_dij)
        self.terheles = terheles

    def __str__(self):
        return f"id: {self.id}, Teherautó: {self.rendszam}, {self.tipus}, {self.berleti_dij}, {self.terheles}"
