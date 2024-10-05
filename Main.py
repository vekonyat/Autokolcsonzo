from Auto import Auto
from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Berles import Berles

kolcsonzo = Autokolcsonzo("Renter")

auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 5000, 5)
auto2 = Szemelyauto("ABC-124", "Honda Civic", 3000, 4)
auto3 = Teherauto("ABC-125", "Ford Transit", 8000, 10)

kolcsonzo.auto_hozzaad(auto1)
kolcsonzo.auto_hozzaad(auto2)
kolcsonzo.auto_hozzaad(auto3)

print(auto1, auto2, auto3)
print(kolcsonzo, kolcsonzo.autok)