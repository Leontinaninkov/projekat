from korisnici.korisnik import registracija, svi_korisnici
from knjige.knjiga import prikazi_knjige, pretrazi_knjige, dodaj_knjigu, izmeni_knjigu, obrisi_knjigu
from akcije.akcija import prikazi_akcije, pretrazi_akcije, dodaj_akciju
from util import menadzer, prodavac, administrator
from kupovina.korpa import dodaj_u_korpu
from knjige.izvestaj import napravi_izvestaj

def meni(ulogovani_korisnik):
    while True:

        print("-" * 20)
        print("1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")


        if administrator(ulogovani_korisnik):
            print('5. Registracija')
            print('6. Svi korisnici')
            print('7. Dodavanje knjige')
            print('8. Izmena Knjige')
            print('9. Brisanje knjige')
        elif menadzer(ulogovani_korisnik):
            print('5. Registracija')
            print('6. Svi korisnici')
            print('7. Dodavanje akcije')
            print('8. Izvestaj')
        elif prodavac(ulogovani_korisnik):
            print('5. Dodavanje knjige')
            print('6. Izmena Knjige')
            print('7. Brisanje knjige')
            print('8. Dodaj u korpu')
        print("0. Odjava")
        print("-" * 20)
        stavka = int(input("Izaberite stavku: "))

        if stavka == 0:
            return
        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5 and administrator(ulogovani_korisnik) or menadzer(ulogovani_korisnik):
            registracija()
        elif stavka == 6 and administrator(ulogovani_korisnik) or menadzer(ulogovani_korisnik):
            svi_korisnici()
        elif (stavka == 5 and prodavac(ulogovani_korisnik)) or \
                (stavka == 7 and administrator(ulogovani_korisnik)):
            dodaj_knjigu()
        elif stavka == 6 and prodavac(ulogovani_korisnik) or \
                (stavka == 8 and administrator(ulogovani_korisnik)):
            izmeni_knjigu()
        elif stavka == 7 and prodavac(ulogovani_korisnik) or \
                (stavka == 9 and administrator(ulogovani_korisnik)):
            obrisi_knjigu()
        elif stavka == 7 and menadzer(ulogovani_korisnik):
            dodaj_akciju()
        elif stavka == 8 and prodavac(ulogovani_korisnik):
            dodaj_u_korpu(ulogovani_korisnik)
        elif stavka == 8 and menadzer(ulogovani_korisnik):
            napravi_izvestaj()


        else:
            print("Pogresan izbor!")
