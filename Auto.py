from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, id, rendszam, tipus, berleti_dij):
        self.id = id
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass