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