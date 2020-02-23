from TrieStruct import *
from parser2 import Parser
from set import Set
from InputParser import *
#from graf import Graph
from graf import *
import time
import os




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
            if str(dirpath + '\\' + fn).endswith('.html'):
                parsed = parser1.parse(dirpath + '\\' + fn)

                #*deo za graf
                p = os.path.join(dirpath, fn)
                p = os.path.abspath(p)
                g.addPage(p, parsed[0])

                print('parsiram:   ' + dirpath + '\\' + fn)
                for word in parser1.words:
                    root.insert(word,os.path.join(dirpath,fn))





    print(root.search("python"))
    end = time.time()
    print(end - start)



    s = ParsirajU(root)# s vraca trazenu listu i niz rijeci iz upita (s,exists)
    s[0].kljucevi()

    if(s[0].Duzina() == 0):
        print("Rezultat pretrage : 0")
    else:
        print("Rezultat pretrage : ")
        s[0].Ispisi()

    rjecnikZaRangiranje = rjecnikZaRang(root, s[1], s[0])
    print("RJECNIK ZA RANGIRANJE PRE UTICAJA LINKOVA")
    if len(rjecnikZaRangiranje)!= 0:
        print(rjecnikZaRangiranje)
    else:
        print("Nema fajlova koji zadovoljavaju pretragu!")



    uticajLinkova(g,s[0],rjecnikZaRangiranje)
    print("RJECNIK POSLE UTICAJA LINKOVA")
    print(rjecnikZaRangiranje)

