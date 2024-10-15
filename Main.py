from Auto import Auto
from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Berles import Berles
from Ugyfel import Ugyfel

kolcsonzo = Autokolcsonzo("Renter")

auto1 = Szemelyauto(1, "ABC-123", "Toyota Corolla", 25000, 5)
auto2 = Szemelyauto(2, "ABC-124", "Honda Civic", 20000, 4)
auto3 = Teherauto(3, "ABC-125", "Ford Transit", 35000, 10)

kolcsonzo.auto_hozzaad(auto1)
kolcsonzo.auto_hozzaad(auto2)
kolcsonzo.auto_hozzaad(auto3)

ugyfel1 = Ugyfel(1, "Nagy Jakab", "AB123456")
ugyfel2 = Ugyfel(2, "Kele Ferenc", "AB123457")
ugyfel3 = Ugyfel(3, "Kiss Mirtill", "AB123458")
ugyfel4 = Ugyfel(4, "Kondor Ottó", "AB123459")

kolcsonzo.ugyfel_hozzaad((ugyfel1))
kolcsonzo.ugyfel_hozzaad((ugyfel2))
kolcsonzo.ugyfel_hozzaad((ugyfel3))
kolcsonzo.ugyfel_hozzaad((ugyfel4))

berles1 = Berles(1,auto1, "2024-02-02", ugyfel1)
berles2 = Berles(2, auto2, "2024-02-04", ugyfel2)
berles3 = Berles(3, auto3, "2024-02-06", ugyfel3)
berles4 = Berles(4, auto1, "2024-02-16", ugyfel4)

kolcsonzo.berles_hozzaad(berles1)
kolcsonzo.berles_hozzaad(berles2)
kolcsonzo.berles_hozzaad(berles3)
kolcsonzo.berles_hozzaad(berles4)

print(kolcsonzo)

while True:
    print("\nKérem, válasszon a következő lehetőségek közül:")
    print("1 - Autó bérlése")
    print("2 - Bérlés lemondása")
    print("3 - Bérlések listázása")
    print("4 - Kilépés")
    valasztas = input("Kérem, válasszon (szám+Enter): ")

    if valasztas == "1":

        while True:
            rendszam = input("Adja meg a bérelni kívánt autó rendszámát: ")
            found_auto = False
            for auto in kolcsonzo.autok:
                if auto.rendszam == rendszam:
                    found_auto = True
                    break
            if found_auto:
                break
            else:
                print("Nincs ilyen rendszámú autó a kölcsönzőben. Próbálja újra.")

        while True:
            datum = input("Adja meg a bérlés dátumát (YYYY-MM-DD): ")
            if kolcsonzo.ervenyes_datum(datum):
                break
            else:
                print("Érvénytelen dátum, kérem adjon meg egy helyes dátumot (YYYY-MM-DD formátumban).")

        while True:
            ugyfel_id = int(input("Adja meg az ügyfélazonosítót: "))
            found_ugyfel = False
            for ugyfel in kolcsonzo.ugyfelek:
                if ugyfel.id == ugyfel_id:
                    found_ugyfel = True
                    break
            if found_ugyfel:
                break
            else:
                print("Hibás ügyfélazonosító. Próbálja újra.")

        # Ha minden érték helyes, bérlés hozzáadása
        if kolcsonzo.berles_hozzaadasa(auto, datum, ugyfel):
            print(f"Sikeres bérlés: {auto.rendszam} - {auto.tipus} bérelve {datum} dátumra {ugyfel.name} számára. Bérleti díj: {auto.berleti_dij} Ft")

    elif valasztas == "2":
        berles_id = int(input("Adja meg a lemondani kívánt bérlés azonosítóját: "))
        kolcsonzo.berles_lemondasa(berles_id)

    elif valasztas == "3":
        kolcsonzo.berlesek_listazasa()

    elif valasztas == "4":
        print(f"Köszönjük, hogy a {kolcsonzo} rendszert használta! Viszontlátásra!")
        break

    else:
        print("Érvénytelen választás, kérem próbálja újra!")
