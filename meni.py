from korisnici.korisnik import prijava, registracija, svi_korisnici
from knjige.knjiga import prikazi_knjige, pretrazi_knjige, dodaj_knjigu, izmeni_knjigu, obrisi_knjigu
from akcije.akcija import prikazi_akcije, pretrazi_akcije
from util import  menadzer, prodavac, admin


def meni(ulogovani_korisnik):
    while True:

        print("-" * 20)
        print("1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("0. Kraj")
        if admin(ulogovani_korisnik):
            print('5. Registracija')
            print('6. Svi korisnici')
            print('7. Dodavanje knjige')
            print('8. Izmena Knjige')
            print('9. Brisanje knjige')
        elif menadzer(ulogovani_korisnik):
            print('5. Registracija')
            print('6. Svi korisnici')
        elif prodavac(ulogovani_korisnik):
            print('5. Dodavanje knjige')
            print('6. Izmena Knjige')
            print('7. Brisanje knjige')

        print("-" * 20)
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5 and admin(ulogovani_korisnik) or menadzer(ulogovani_korisnik):
            registracija()
        elif stavka == 6 and admin(ulogovani_korisnik) or menadzer(ulogovani_korisnik):
            svi_korisnici()
        elif (stavka == 5 and prodavac(ulogovani_korisnik)) or \
                (stavka == 7 and admin(ulogovani_korisnik)):
            dodaj_knjigu()
        elif stavka == 6 and prodavac(ulogovani_korisnik) or \
                (stavka == 8 and admin(ulogovani_korisnik)):
            izmeni_knjigu()
        elif stavka == 7 and prodavac(ulogovani_korisnik) or \
                (stavka == 9 and admin(ulogovani_korisnik)):
            obrisi_knjigu()
        elif stavka == 0:
            return
        else:
            print("Pogresan izbor!")
