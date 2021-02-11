from akcije.akcija import ucitaj_akcije, ispisi_akcije
from knjige.knjiga import ucitaj_knjige, ispisi_knjige
from datetime import datetime
from kupovina.racunIO import sacuvaj_racune, ucitaj_racune
from akcije.akcijaIO import sacuvaj_akcije

korpa = {}

def dodaj_u_korpu(korisnik):

    korpa = {}
    akcije_korpa = {}
    while True:

        print("-" * 20)
        print("1. Dodaj knjigu")
        print("2. Dodaj akciju")
        print("3. Napravi Racun")
        print("4. Isprazni korpu")
        print("5. Prikazi korpu")
        print("-" * 20)
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            dodavanje_knjige()
        elif stavka == 2:
            korpa_akcije = dodavanje_akcije()
            for sifra in korpa_akcije.keys():
                if sifra not in akcije_korpa.keys():
                    akcije_korpa[sifra] = korpa_akcije[sifra]
                else:
                    akcije_korpa[sifra] += korpa_akcije[sifra]
        elif stavka == 3:
            napravi_racun(korisnik, akcije_korpa)
            break
        elif stavka == 5:
            prikazi_korpu()

    korpa = {}


def prikazi_korpu():
    knjige = ucitaj_knjige()

    zaglavlje = f"{'knjiga':<30}" \
                f"{'kolicina':<10}" \
                f"{'cena':<10}"

    print(zaglavlje)
    print("-" * len(zaglavlje))
    ukupna_cena = 0
    for sifra in korpa.keys():
        for knjiga in knjige:
            if knjiga['sifra'] == int(sifra):
                za_ispis = f"{knjiga['naslov']:<30}" \
                           f"{korpa[sifra]['kolicina']:<10}" \
                           f"{korpa[sifra]['cena']:<10}"
                ukupna_cena += korpa[sifra]['cena']

                print(za_ispis)
    print('-' * 20)
    print(f'Ukupna cena: {ukupna_cena}')
    print("-" * len(zaglavlje))


def dodavanje_akcije():

    knjige = ucitaj_knjige()
    akcije = ucitaj_akcije()
    ispisi_akcije(akcije, knjige)

    akcije_korpa = {}
    while True:
        sifra = int(input("Unesite [sifra] za kupovinu knjiga iz akcije ili [0] za izlaz: "))
        if sifra == 0:
            break
        for akcija in akcije:
            if akcija['sifra'] == sifra and datetime.strptime(akcija['datum'], f'%d/%m/%Y') >= datetime.today():
                if str(sifra) not in akcije_korpa.keys():
                    akcije_korpa[sifra] = 1
                else:
                    akcije_korpa[sifra] +=1

                for knjiga_id in akcija['ponuda'].keys():
                    print(f'{knjiga_id} {korpa.keys()}')
                    if knjiga_id not in korpa.keys():
                        korpa[knjiga_id] = {'kolicina': 1, 'cena': akcija['ponuda'][knjiga_id]}
                    else:
                        korpa[knjiga_id]['cena'] += akcija['ponuda'][knjiga_id]
                        korpa[knjiga_id]['kolicina'] += 1
                break

    return akcije_korpa

def dodavanje_knjige():

    knjige = ucitaj_knjige()
    ispisi_knjige(knjige)

    while True:
        sifra_kolicna = input("Unesite [sifra:kolicina] za kupovinu knjige ili [0] za izlaz: ")
        if sifra_kolicna == '0':
            break
        sifra = int(sifra_kolicna.split(':')[0])
        kolicina = int(sifra_kolicna.split(':')[1])
        for knjiga in knjige:
            if knjiga['sifra'] == sifra:

                if str(sifra) not in korpa.keys():
                    korpa[str(sifra)] = {'kolicina': kolicina, 'cena': knjiga['cena'] * kolicina}
                else:
                    korpa[str(sifra)]['cena'] += knjiga['cena'] * kolicina
                    korpa[str(sifra)]['kolicina'] += kolicina
                break


def napravi_racun(korisnik, akcije_korpa):
    racuni = ucitaj_racune()
    akcije = ucitaj_akcije()
    for akcija_sifra in akcije_korpa:
        for akcija in akcije:
            if akcija['sifra'] == akcija_sifra:
                akcija['kupljena'] += 1

    sacuvaj_akcije(akcije)

    maks = racuni[0]['sifra']

    for racun in racuni:
        if racun['sifra'] > maks:
            maks = racun['sifra']

    maks += 1

    racun = {'sifra': maks, 'prodavac': korisnik['korisnicko_ime'],
             'datum_vreme': datetime.now().strftime(f"%d/%m/%Y, %H:%M:%S"), 'korpa': korpa}
    racuni.append(racun)
    sacuvaj_racune(racuni)