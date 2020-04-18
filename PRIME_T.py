import math

def od_do(od, do):
        zw = []
        while od!=do+1:
            zw.append(od)
            od+=1
        return zw

def sito(do):
    sq = int(math.sqrt(do))  # gorny zakres dzialania algorytmu

    obecnie = 2  # wartosc poczatkowa
    tab = od_do(2, do)  # utworz tablice z wartosciami od 1 do "do"
    while True:
        if obecnie > sq:  # warunek zakonczenia dzialania algorytmu
            return tab

        for i in tab:  # dla wszystkich liczb w tablicy
            # usun element jezeli jest podzielny przez obecna liczbe
            if (not (i % obecnie) and not (obecnie == i)) and obecnie != 1:
                tab.remove(i)

        i = tab.index(obecnie) + 1
        obecnie = tab[i]

primes = sito(10000)

n = int(input())
for i in range(n):
    x = int(input())
    if x in primes: print("TAK")
    else: print("NIE")
