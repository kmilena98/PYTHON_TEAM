from TrieStruct import *
from parser2 import Parser
from set import Set
from InputParser import *
#from graf import Graph
from graf import *
import time
import os
from rangiranje import *
from sortiranje import *
from paginacija import *
#python-2.7.7-docs-html



if __name__ == "__main__":
    print("Trenutni direktorijum je: " + os.getcwd())
    print("Unesite direktorijum koji zelite da parsirate: ")
    dir = input()

    while (not os.path.isdir(dir)):
        print("Ne postoji uneti direktorijum")
        dir = input()

    parser1 = Parser()
    root = Trie()
    #root1 = TrieNode()
    links = []
    start = time.time()
    g = Graph()
    for dirpath, dirnames, files in os.walk(str(dir)):
        print(f'Found directory: {dirpath}')
        for fn in files:
            if str(dirpath + '//' + fn).endswith('.html'):
                parsed = parser1.parse(dirpath + '//' + fn)

                #*deo za graf
                p = os.path.join(dirpath, fn)
                p = os.path.abspath(p)
                g.addPage(p, parsed[0])

                print('parsiram:   ' + dirpath + '//' + fn)

                for word in parser1.words:
                    root.insert(word,dirpath + '//' + fn)





    #print(root.search("python"))
    end = time.time()
    print(end - start)



    s = ParsirajU(root)# s vraca trazenu listu i niz rijeci iz upita (s,exists)
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
    rjecnikZaRangiranje = rjecnikZaRang(root, s[1], s[0]) # uticaj broja reci koji se pojavljuje u datom linku
    #print("RJECNIK ZA RANGIRANJE PRE UTICAJA LINKOVA")
    if len(rjecnikZaRangiranje)!= 0:
        print(rjecnikZaRangiranje)
        print("********************************************************************")
    #2
        uticajVrednostiLinkova(g, s[0], rjecnikZaRangiranje)
        print("RJECNIK POSLE UTICAJA LINKOVA")
        print(rjecnikZaRangiranje)
    #3
        '''
        uticajBrojaLinkova(root, g, rjecnikZaRangiranje, s[1])
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
        '''

    else:
        print("Nema fajlova koji zadovoljavaju pretragu!")








