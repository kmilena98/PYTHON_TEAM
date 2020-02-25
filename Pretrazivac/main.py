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
            r = rjecnikZaRang(trie, s[1], s[0])
            #normalanBroj je lista linkova i br reci u njima
            rjecnikZaRangiranje = r[0]
            normalanBroj = {}
            normalanBroj2 = {}
            for k in rjecnikZaRangiranje.keys():
                normalanBroj[k] = rjecnikZaRangiranje[k]
                normalanBroj2[k] = rjecnikZaRangiranje[k]



            rang1 = {}
            rang1 = uticajRazlicitihReci(r[1], normalanBroj)
            # u rang1 se nalazi koji je stepen upitanju
            uticajRazReci = {}
            for k in rjecnikZaRangiranje.keys():
                uticajRazReci[k] = rjecnikZaRangiranje[k]


            rang2 = {}
            w = uticajBrojaReci(rjecnikZaRangiranje)
            uticajReci = {}
            for k in rjecnikZaRangiranje.keys():
                rang2[k] = w[k]


            rang3 = {}

            m= uticajVrednostiLinkova(g, rjecnikZaRangiranje.keys(), normalanBroj)

            for k in rjecnikZaRangiranje.keys():
                rang3[k] = m[k]

            rang4 = {}
            p = uticajBrojaLinkova(trie, g, rjecnikZaRangiranje, s[1])
            for k in rjecnikZaRangiranje.keys():
                rang4[k] = p[k]

            RANG = {}
            for r in rjecnikZaRangiranje.keys():
                RANG[r] = rang1[r]-rang2[r]-rang3[r]-rang4[r]
            if len(rjecnikZaRangiranje)!= 0:

                #("RANG\t\tBR RECI\t\tR1\t\t\tR2\printt\t\tR3\t\t\tR4\t\t\t\t\t\t\t\t\t\t\tlink" )
                #for a in rjecnikZaRangiranje.keys():
                    #cvor = Ispis(normalanBroj2[a],rang1[a],rang2[a],rang3[a],rang4[a],RANG[a],a)
                    #cvor.Ispisi()

                listaZaSortiranje = []
                for strana in rjecnikZaRangiranje.keys():
                    listaZaSortiranje.append(PageRang(strana,RANG[strana]))

                #SORTIRANJE
                heap_sort(listaZaSortiranje)
                #print("************************************")
                #print("Sortirani rangocvi su:")
                #for i in listaZaSortiranje:
                #    print(i.getPage(),i.getRang())

                #PAGINACIJA
                paginacija(listaZaSortiranje,normalanBroj2,rang1,rang2,rang3,rang4)


            else:
                print("Nema fajlova koji zadovoljavaju pretragu!")



        elif unos == "0":
            break









