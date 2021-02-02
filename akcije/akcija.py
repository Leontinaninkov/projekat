from akcije.akcijaIO import ucitaj_akcije
from knjige.knjigaIO import ucitaj_knjige
from util import bubble_sort, bubble_sort_dt


def prikazi_akcije():

    print("-" * 20)
    print("1. Sortiranje po sifri")
    print("2. Sortiranje po datumu")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    akcije = ucitaj_akcije()
    knjige = ucitaj_knjige()
    if stavka == 1:
        bubble_sort(akcije, "sifra")
    elif stavka == 2:
        bubble_sort_dt(akcije, "datum")

    ispisi_akcije(akcije, knjige)


def pretrazi_akcije():
    print()
    print("-" * 20)
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu knjige")
    print("3. Pretraga po autoru knjige")
    print("4. Pretraga po kategoriji knjige")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    akcije = []
    knjige = ucitaj_knjige()
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_sifra("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite naslov: ")
        akcije = pretraga_akcija_string("naslov", naslov)
    elif stavka == 3:
        autor = input("Unesite autora: ")
        akcije = pretraga_akcija_string("autor", autor)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju: ")
        akcije = pretraga_akcija_string("kategorija", kategorija)

    ispisi_akcije(akcije, knjige)


def pretraga_akcija_sifra(kljuc, vrednost):
    akcije = ucitaj_akcije()
    pronadjene_akcije = []

    for akcija in akcije:
        if (akcija[kljuc] == int(vrednost)):
            pronadjene_akcije.append(akcija)

    return pronadjene_akcije


def pretraga_akcija_jednakost(kljuc, vrednost):
    akcije = ucitaj_akcije()
    knjige = ucitaj_knjige()
    pronadjene_akcije = []
    pronadjen = False
    for akcija in akcije:
        for ponuda in akcija['ponuda'].keys():
            for knjiga in knjige:
                if knjiga['sifra'] == int(ponuda) and knjiga[kljuc] == vrednost:
                    pronadjene_akcije.append(akcija)
                    pronadjen = True
                    break

            if pronadjen:
                break;

    return pronadjene_akcije


def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    knjige = ucitaj_knjige()
    pronadjene_akcije = []
    pronadjen = False
    for akcija in akcije:
        for ponuda in akcija['ponuda'].keys():
            for knjiga in knjige:
                if knjiga['sifra'] == int(ponuda) and vrednost.lower() in knjiga[kljuc].lower():
                    pronadjene_akcije.append(akcija)
                    pronadjen = True
                    break

            if pronadjen:
                break;

    return pronadjene_akcije


def ispisi_akcije(akcije, knjige):

    nl = '\n\t\t\t'
    tab = '\t'
    zaglavlje = f"{'sifra':<10}" \
                f"{'datum':<20}" \
                f"{tab} {'knjige':<60}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for akcija in akcije:
        za_ispis = f"{akcija['sifra']:<10}" \
                   f"{akcija['datum']:<20}"
        for ponuda in akcija['ponuda'].keys():
            for knjiga in knjige:
                if (knjiga['sifra'] == int(ponuda)):
                    za_ispis += f"{tab} {knjiga['naslov']}=> cena: {knjiga['cena']} -> cena sa popustom: {akcija['ponuda'][ponuda]}{nl}"

        print(za_ispis)
    print("-" * len(zaglavlje))