from korisnici.korisnik import prijava
from meni import meni


def main():
    ulogovani_korisnik = None,
    while ulogovani_korisnik == None:

        ulogovani_korisnik = prijava()

        if ulogovani_korisnik is not None:
            break
        else:
            print("Pogresno korisnicko ime ili lozinka!\n")

    meni(ulogovani_korisnik)


if __name__ == "__main__":
    main()