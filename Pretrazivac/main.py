from StrukturePodataka.TrieStruct import *
from Funkcionalnosti.parser2 import Parser
from StrukturePodataka.set import Set
from Funkcionalnosti.InputParser import *
#from graf import Graph
from StrukturePodataka.graf import *
import time
import os
from Funkcionalnosti.rangiranje import *
from Funkcionalnosti.sortiranje import *
from Funkcionalnosti.paginacija import *
#python-2.7.7-docs-html


def menu():
    print("*********************")
    print("\tIzaberite opciju: ")
    print("1. Promenite direktorijum ")
    print("2. Unesite upit za pretragu ")
    print("0. Izlaz")
    print("*********************")
    unos = input("Izaberite opciju : ")
    return unos

if __name__ == "__main__":
    print("Trenutni direktorijum je: " + os.getcwd())
    print("Unesite direktorijum koji zelite da parsirate: ")
    dir = input()

    while (not os.path.isdir(dir)):
        print("Ne postoji uneti direktorijum,unesite novi:")
        dir = input()

    if not os.path.isabs(dir):
        dir = os.path.abspath(dir)
    parser1 = Parser()
    trie = Trie()

    start = time.time()
    g = Graph()
    for dirpath, dirnames, files in os.walk(str(dir)):
        #print(f'Pronadjen direktorijum: {dirpath}')
        for fn in files:

            if str(dirpath + '//' + fn).endswith('.html'):
                parsed = parser1.parse(dirpath + '//' + fn)

            if fn.endswith('.html') or fn.endswith('.htm'):
                absPath = os.path.join(dirpath, fn)
                parsed = parser1.parse(absPath)

                g.addPage(absPath, parsed[0])

                print('parsiram:   ' + dirpath + '//' + fn)

                for word in parser1.words:
                    trie.insert(word,dirpath + '//' + fn)

                #print('parsiram:   ' + dirpath + '\\' + fn)
                for word in parser1.words:
                    trie.insert(word,absPath)

    end = time.time()
    print(end - start)
    unos = 1
    while unos != 0:
        unos = menu()
        if unos == "1":
            trie = Trie()
            g = Graph()
            print("Trenutni direktorijum je: " + os.getcwd())
            print("Unesite direktorijum koji zelite da parsirate: ")
            dir = input()

            while (not os.path.isdir(dir)):
                print("Ne postoji uneti direktorijum,unesite novi:")
                dir = input()
            if not os.path.isabs(dir):
                dir = os.path.abspath(dir)
            start = time.time()

            for dirpath, dirnames, files in os.walk(str(dir)):
                #print(f'Pronadjen direktorijum: {dirpath}')
                for fn in files:
                    if fn.endswith('.html') or fn.endswith('.htm'):
                        absPath = os.path.join(dirpath, fn)
                        parsed = parser1.parse(absPath)

                        g.addPage(absPath, parsed[0])

                        for word in parser1.words:
                            trie.insert(word,absPath)
            end = time.time()
            print(end - start)
        elif unos == "2":
            s = ParsirajU(trie) # s vraca trazenu listu i niz rijeci iz upita (s,exists)
#1
            rjecnikZaRangiranje = rjecnikZaRang(trie, s[1], s[0]) # uticaj broja reci koji se pojavljuje u datom linku
            print("RJECNIK ZA RANGIRANJE PRE UTICAJA LINKOVA")
            if len(rjecnikZaRangiranje)!= 0:
                print(rjecnikZaRangiranje)
            #2
                uticajVrednostiLinkova(g, s[0], rjecnikZaRangiranje)
                print("RJECNIK POSLE UTICAJA LINKOVA")
                print(rjecnikZaRangiranje)
            #3

                uticajBrojaLinkova(trie, g, rjecnikZaRangiranje, s[1])

                uticajBrojaLinkova(trie, g, rjecnikZaRangiranje, s[1])
                print("RJECNIK POSLE UTICAJA LINKOVA")
                print(rjecnikZaRangiranje)
                # u rjecnikZaRangiranje se nalazi rjecnik, kljucevi su linkovi a vrednosti su rangovi

                listaZaSortiranje = []
                for strana in rjecnikZaRangiranje.keys():
                    listaZaSortiranje.append(PageRang(strana,rjecnikZaRangiranje[strana]))

                heap_sort(listaZaSortiranje)
                print("************************************")
                print("Sortirani rangocvi su:")
                for i in listaZaSortiranje:
                    print(i.getPage(),i.getRang())

                paginacija(listaZaSortiranje)


            else:
                print("Nema fajlova koji zadovoljavaju pretragu!")



        elif unos == "0":
            break

    s = ParsirajU(trie)# s vraca trazenu listu i niz rijeci iz upita (s,exists)
    s[0].kljucevi()
    print()
    print("********************************************************************")
    if(s[0].Duzina() == 0):
        print("Rezultat pretrage : 0")
    else:
        print("Rezultat pretrage : ")
        s[0].Ispisi()
    print("********************************************************************")
    print("rjecnik:")
    #1
    rjecnikZaRangiranje = rjecnikZaRang(trie, s[1], s[0]) # uticaj broja reci koji se pojavljuje u datom linku
    #print("RJECNIK ZA RANGIRANJE PRE UTICAJA LINKOVA")
    if len(rjecnikZaRangiranje)!= 0:
        print(rjecnikZaRangiranje)
        print("********************************************************************")
    #2
        uticajVrednostiLinkova(g, s[0], rjecnikZaRangiranje)
        print("RJECNIK POSLE UTICAJA LINKOVA")
        print(rjecnikZaRangiranje)
    #3

        uticajBrojaLinkova(trie, g, rjecnikZaRangiranje, s[1])
        print("RJECNIK POSLE UTICAJA LINKOVA")
        print(rjecnikZaRangiranje)
        # u rjecnikZaRangiranje se nalazi rjecnik, kljucevi su linkovi a vrednosti su rangovi

        listaZaSortiranje = []
        for strana in rjecnikZaRangiranje.keys():
            listaZaSortiranje.append(PageRang(strana,rjecnikZaRangiranje[strana]))

        heap_sort(listaZaSortiranje)
        print("Sortirani rangocvi su:")
        for i in listaZaSortiranje:
            print(i.getPage(),i.getRang())

        paginacija(listaZaSortiranje)










