from kupovina.racunIO import ucitaj_racune
from knjige.knjigaIO import ucitaj_knjige
from knjige.knjiga import ispisi_knjige
from akcije.akcijaIO import ucitaj_akcije


def napravi_izvestaj():
    print()
    print('Izvestaj prodaje')
    print("-" * 20)
    print("1. Prodaja svih knjiga")
    print("2. Prodaja svih akcija")
    print("3. Prodaja knjiga po autoru")
    print("4. Prodaja knjiga po izdavacu")
    print("5. Prodaja knjiga po kategoriji")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    racuni = ucitaj_racune()
    if stavka == 1:
        izvestaj_svih_knjiga(racuni)
    elif stavka == 2:
        izvestaj_svih_akcija()
    elif stavka == 3:
        izvestaj_po_autoru(racuni)
    elif stavka == 4:
        izvestaj_po_izdavacu(racuni)
    elif stavka == 5:
        izvestaj_po_kategoriji(racuni)


def izvestaj_svih_akcija():
    izvestaj = {}
    akcije = ucitaj_akcije()
    knjige = ucitaj_knjige()
    for akcija in akcije:
        if akcija['kupljena'] > 0:
            for sifra in akcija['ponuda'].keys():
                for knjiga in knjige:
                    if knjiga['sifra'] == int(sifra):
                        if sifra not in izvestaj.keys():
                            izvestaj[sifra] = {'naslov': knjiga['naslov'], 'kolicina': akcija['kupljena'],
                                               'zarada': akcija['ponuda'][sifra] * akcija['kupljena']}
                        else:
                            izvestaj[sifra]['kolicina'] += akcija['kupljena']
                            izvestaj[sifra]['zarada'] += akcija['ponuda'][sifra] * akcija['kupljena']

    ispisi_izvestaj(izvestaj)




def izvestaj_po_kategoriji(racuni):
    knjige = ucitaj_knjige()
    ispisi_knjige(knjige)

    kategorija = input("Unesite kategoriju: ")

    izvestaj = {}
    for racun in racuni:
        for sifra in racun['korpa'].keys():
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra) and kategorija.lower() in knjiga['kategorija'].lower():
                    if sifra not in izvestaj.keys():
                        izvestaj[sifra] = {'naslov': knjiga['naslov'], 'kolicina': racun['korpa'][sifra]['kolicina'],
                                           'zarada': racun['korpa'][sifra]['cena']}
                    else:
                        izvestaj[sifra]['kolicina'] += racun['korpa'][sifra]['kolicina']
                        izvestaj[sifra]['zarada'] += racun['korpa'][sifra]['cena']

    ispisi_izvestaj(izvestaj)


def izvestaj_po_izdavacu(racuni):
    knjige = ucitaj_knjige()
    ispisi_knjige(knjige)

    izdavac = input("Unesite izdavaca: ")

    izvestaj = {}
    for racun in racuni:
        for sifra in racun['korpa'].keys():
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra) and izdavac.lower() in knjiga['izdavac'].lower():
                    if sifra not in izvestaj.keys():
                        izvestaj[sifra] = {'naslov': knjiga['naslov'], 'kolicina': racun['korpa'][sifra]['kolicina'],
                                           'zarada': racun['korpa'][sifra]['cena']}
                    else:
                        izvestaj[sifra]['kolicina'] += racun['korpa'][sifra]['kolicina']
                        izvestaj[sifra]['zarada'] += racun['korpa'][sifra]['cena']

    ispisi_izvestaj(izvestaj)


def izvestaj_po_autoru(racuni):
    knjige = ucitaj_knjige()
    ispisi_knjige(knjige)

    autor = input("Unesite autora: ")

    izvestaj = {}
    for racun in racuni:
        for sifra in racun['korpa'].keys():
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra) and autor.lower() in knjiga['autor'].lower():
                    if sifra not in izvestaj.keys():
                        izvestaj[sifra] = {'naslov': knjiga['naslov'], 'kolicina': racun['korpa'][sifra]['kolicina'],
                                           'zarada': racun['korpa'][sifra]['cena']}
                    else:
                        izvestaj[sifra]['kolicina'] += racun['korpa'][sifra]['kolicina']
                        izvestaj[sifra]['zarada'] += racun['korpa'][sifra]['cena']

    ispisi_izvestaj(izvestaj)


def izvestaj_svih_knjiga(racuni):
    knjige = ucitaj_knjige()
    izvestaj = {}
    for racun in racuni:
        for sifra in racun['korpa'].keys():
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra):
                    if sifra not in izvestaj.keys():
                        izvestaj[sifra] = {'naslov': knjiga['naslov'], 'kolicina': racun['korpa'][sifra]['kolicina'],
                                           'zarada': racun['korpa'][sifra]['cena']}
                    else:
                        izvestaj[sifra]['kolicina'] += racun['korpa'][sifra]['kolicina']
                        izvestaj[sifra]['zarada'] += racun['korpa'][sifra]['cena']

    ispisi_izvestaj(izvestaj)


def ispisi_izvestaj(izvestaj):

    zaglavlje = f"{'naslov':<30}" \
                f"{'kolicina':<10}" \
                f"{'zarada':<10}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for sifra in izvestaj.keys():
        za_ispis = f"{izvestaj[sifra]['naslov']:<30}" \
                   f"{izvestaj[sifra]['kolicina']:<10}" \
                   f"{izvestaj[sifra]['zarada']:<10}"
        print(za_ispis)

    print("-" * len(zaglavlje))