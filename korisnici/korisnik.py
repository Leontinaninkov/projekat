from korisnici.korisnikIO import ucitaj_korisnike, sacuvaj_korisnike
from util import bubble_sort

def prijava():
    korisnici = ucitaj_korisnike()

    korisnicko_ime = input("korisnicko ime: ")
    lozinka = input("lozinka: ")

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka'] == lozinka:
            return korisnik
    return None


def registracija():
    korisnici = ucitaj_korisnike()
    korisnicko_ime = None
    while (True):

        korisnicko_ime = input('Korisnicko ime: ')
        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime:
                continue
        break

    lozinka = input('Lozinka: ')
    ime = input('Ime: ')
    prezime = input('Prezime: ')

    tip_korisnika = None
    while (True):
        tip_korisnika = input('Tip korisnika: ')
        if (tip_korisnika == 'prodavac' or tip_korisnika == 'menadzer'):
            break
        continue

    korisnici.append({'korisnicko_ime': korisnicko_ime,
                      'lozinka': lozinka,
                      'ime': ime,
                      'prezime': prezime,
                      'tip_korisnika': tip_korisnika
                      })
    sacuvaj_korisnike(korisnici)


def svi_korisnici():
    print("-" * 20)
    print("1. Sortiranje po imenu")
    print("2. Sortiranje po prezimenu")
    print("3. Sortiranje po tipu korisnika")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    korisnici = ucitaj_korisnike()

    if stavka == 1:
        bubble_sort(korisnici, "ime")
    elif stavka == 2:
        bubble_sort(korisnici, "prezime")
    elif stavka == 3:
        bubble_sort(korisnici, "tip_korisnika")
    else:
        print('pogresna stavka!')
        return

    ispisi_korisnike(korisnici)

def ispisi_korisnike(korisnici):

    zaglavlje = f"{'korisnicko ime':<20}" \
               f"{'ime':<20}" \
               f"{'prezime':<20}" \
               f"{'tip korisnika':<20}"
    print(zaglavlje)
    print("-"*len(zaglavlje))

    for korisnik in korisnici:

        za_ispis = f"{korisnik['korisnicko_ime']:<20}" \
                   f"{korisnik['ime']:<20}" \
                   f"{korisnik['prezime']:<20}" \
                   f"{korisnik['tip_korisnika']:<20}"
        print(za_ispis)