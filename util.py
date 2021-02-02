from datetime import datetime

def bubble_sort(lista, kljuc):
    n = len(lista)
    for j in range(n):
        for i in range(n - 1 - j):
            if lista[i][kljuc] > lista[i + 1][kljuc]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


def bubble_sort_dt(lista, kljuc):
    n = len(lista)
    for i in range(0, n - 1):
        for j in range(i + 1, n):

            if datetime.strptime(lista[i][kljuc], f'%d/%m/%Y') > datetime.strptime(lista[j][kljuc], f'%d/%m/%Y'):
                lista[i], lista[j] = lista[j], lista[i]

def menadzer(ulogovani_korisnik):
    return ulogovani_korisnik['tip_korisnika'] == 'menadzer'


def prodavac(ulogovani_korisnik):
    return ulogovani_korisnik['tip_korisnika'] == 'prodavac'


def admin(ulogovani_korisnik):
    return ulogovani_korisnik['tip_korisnika'] == 'administrator'