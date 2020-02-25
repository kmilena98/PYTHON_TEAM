from StrukturePodataka.TrieStruct import *
from StrukturePodataka.set import Set
from StrukturePodataka.ispis import *
from Funkcionalnosti.parser2 import Parser
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
    print("\tIzaberite sadrzaj: ")
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
            r = rjecnikZaRang(trie, s[1], s[0]) # uticaj broja reci koji se pojavljuje u datom linku
            rjecnikZaRangiranje = r[0]
            ## r[1] je broj razlicitih reci na linku
            if len(rjecnikZaRangiranje)!= 0:
                uticajBrojaReci(rjecnikZaRangiranje)
                uticajReci = {}
                for k in rjecnikZaRangiranje.keys():
                    uticajReci[k] = rjecnikZaRangiranje[k]
                #print("1. UTICAJ RECI U LINKU")
                #print(rjecnikZaRangiranje)
                #print("---------------------------------------------------------------")
            #2
               # print("---------------------------------------------------------------")

                uticajVrednostiLinkova(g, rjecnikZaRangiranje.keys(), rjecnikZaRangiranje)
                uticajVLinkova = {}
                for k in rjecnikZaRangiranje.keys():
                    uticajVLinkova[k] = rjecnikZaRangiranje[k]
                #print("2.UTICAJ VREDNOSTI LINKOVA")
                #print(rjecnikZaRangiranje)
                #print("---------------------------------------------------------------")
            #3
                #print("---------------------------------------------------------------")
                uticajRazlicitihReci(r[1],rjecnikZaRangiranje)
                uticajRazReci = {}
                for k in rjecnikZaRangiranje.keys():
                    uticajRazReci[k] = rjecnikZaRangiranje[k]
                #print("3.UTICAJ RAZLICITIH RECI U LINKOVIMA")
                #print(rjecnikZaRangiranje)
                #print("---------------------------------------------------------------")
            #4
                print(
                    "----------------------------------------------------------------------------------------------------------------------------")
                uticajBrojaLinkova(trie, g, rjecnikZaRangiranje, s[1])
                uticajBrLinkova = {}
                for k in rjecnikZaRangiranje.keys():
                    uticajBrLinkova[k] = rjecnikZaRangiranje[k]
                #print("4. UTICAJ BROJA LINKOVA")
                #print(rjecnikZaRangiranje)
                print("----------------------------------------------------------------------------------------------------------------------------")
                # u rjecnikZaRangiranje se nalazi rjecnik, kljucevi su linkovi a vrednosti su rangovi

                print("R1       R2      R3      R4                                    link" )
                for a in rjecnikZaRangiranje.keys():
                    cvor = Ispis(uticajReci[a],uticajVLinkova[a],uticajRazReci[a],uticajBrLinkova[a],a)
                    cvor.Ispisi()

                listaZaSortiranje = []
                for strana in rjecnikZaRangiranje.keys():
                    listaZaSortiranje.append(PageRang(strana,rjecnikZaRangiranje[strana]))

                #SORTIRANJE
                heap_sort(listaZaSortiranje)
                #print("************************************")
                #print("Sortirani rangocvi su:")
                #for i in listaZaSortiranje:
                #    print(i.getPage(),i.getRang())

                #PAGINACIJA
                paginacija(listaZaSortiranje)


            else:
                print("Nema fajlova koji zadovoljavaju pretragu!")



        elif unos == "0":
            break









