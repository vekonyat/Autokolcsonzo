from Auto import Auto
from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Berles import Berles
from Ugyfel import Ugyfel

kolcsonzo = Autokolcsonzo("Renter")

auto1 = Szemelyauto(1, "ABC-123", "Toyota Corolla", 5000, 5)
auto2 = Szemelyauto(2, "ABC-124", "Honda Civic", 3000, 4)
auto3 = Teherauto(3, "ABC-125", "Ford Transit", 8000, 10)

kolcsonzo.auto_hozzaad(auto1)
kolcsonzo.auto_hozzaad(auto2)
kolcsonzo.auto_hozzaad(auto3)

ugyfel1 = Ugyfel(1, "Nagy Jakab", "AB123456")
ugyfel2 = Ugyfel(1, "Kele Ferenc", "AB123457")
ugyfel3 = Ugyfel(1, "Kiss Mirtill", "AB123458")
ugyfel4 = Ugyfel(1, "Kondor Ottó", "AB123459")

kolcsonzo.ugyfel_hozzaad((ugyfel1))
kolcsonzo.ugyfel_hozzaad((ugyfel2))
kolcsonzo.ugyfel_hozzaad((ugyfel3))
kolcsonzo.ugyfel_hozzaad((ugyfel4))

berles1 = Berles(1,auto1, "2024-02-02", 1)
berles2 = Berles(1, auto2, "2024-02-04", 2)
berles3 = Berles(1, auto3, "2024-02-06", 3)
berles4 = Berles(1, auto1, "2024-02-16", 4)

kolcsonzo.berles_hozzaad(berles1)
kolcsonzo.berles_hozzaad(berles2)
kolcsonzo.berles_hozzaad(berles3)
kolcsonzo.berles_hozzaad(berles4)

print(auto1, auto2, auto3)
print("\n", kolcsonzo.autok[0],"\n", kolcsonzo.berlesek[0])