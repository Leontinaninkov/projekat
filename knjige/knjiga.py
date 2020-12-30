from knjige.knjigaIO import ucitaj_knjige
from util import bubble_sort

def prikazi_knjige():
    print("-"*20)
    print("1. Sortiranje po naslovu")
    print("2. Sortiranje po autoru")
    print("3. Sortiranje po kategoriji")
    print("4. Sortiranje po izdavacu")
    print("5. Sortiranje po ceni")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    knjige = ucitaj_knjige()

    if stavka == 1:
        bubble_sort(knjige, "naslov")
    elif stavka == 2:
        bubble_sort(knjige, "autor")
    elif stavka == 3:
        bubble_sort(knjige, "kategorija")
    elif stavka == 4:
        bubble_sort(knjige, "izdavac")
    elif stavka == 5:
        bubble_sort(knjige, "cena")
    ispisi_knjige(knjige)

def pretrazi_knjige():

    print("-"*20)
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("5. Pretraga po izdavacu")
    print("6. Pretraga po ceni")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    knjige = []

    if stavka == 1:
        sifra = input("Unesite sifru: ")
        knjige = pretraga_knjiga_jednakost("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite naslov: ")
        knjige = pretraga_knjiga_string("naslov", naslov)
    elif stavka == 3:
        autor = input("Unesite autora: ")
        knjige = pretraga_knjiga_string("autor", autor)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretraga_knjiga_string("kategorija", kategorija)
    elif stavka == 5:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretraga_knjiga_string("izdavac", izdavac)

    ispisi_knjige(knjige)


def pretraga_knjiga_jednakost(kljuc, vrednost):
    knjige = ucitaj_knjige()
    pronadjene_knjige = []

    for knjiga in knjige:
        if knjiga[kljuc] == vrednost:
            pronadjene_knjige.append(knjiga)

    return pronadjene_knjige


def pretraga_knjiga_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    pronadjene_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            pronadjene_knjige.append(knjiga)

    return pronadjene_knjige


def ispisi_knjige(knjige):
    zaglavlje = f"{'sifra':<10}" \
               f"{'naslov':<20}" \
               f"{'autor':<20}" \
               f"{'isbn':^20}" \
               f"{'izdavac':^20}" \
               f"{'godina izdanja':^20}" \
               f"{'broj strana':^20}" \
               f"{'cena':^20}" \
               f"{'kategorija':^20}"
    print(zaglavlje)
    print("-"*len(zaglavlje))

    for knjiga in knjige:

        za_ispis = f"{knjiga['sifra']:<10}" \
                   f"{knjiga['naslov']:<20}" \
                   f"{knjiga['autor']:<20}" \
                   f"{knjiga['isbn']:^20}" \
                   f"{knjiga['izdavac']:^20}" \
                   f"{knjiga['godina_izdanja']:^20}" \
                   f"{knjiga['broj_strana']:^20}" \
                   f"{knjiga['cena']:^20}" \
                   f"{knjiga['kategorija']:^20}"
        print(za_ispis)


