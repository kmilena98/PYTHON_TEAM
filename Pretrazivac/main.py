from TrieStruct import *
from parser2 import Parser
from set import Set
from InputParser import ParsirajU
from graf import Graph
import time
import os

def ucitajUGraf(path):
    g = Graph()
    mojParser = Parser()
    for subdir, dirs, files in os.walk(path):
        for name in files:
                 if name.endswith('.html'):
                     links,words = mojParser.parse(os.path.join(subdir,name))
                     #self.build(os.path.join(subdir,name),words)
                     g.dodajCvor(name,links,words,os.path.join(subdir,name))

    print("DODAVANJE U GRAF ZAVRSENO")
    return g



if __name__ == "__main__":
    print("Trenutni direktorijum je: " + os.getcwd())
    print("Unesite direktorijum koji zelite da parsirate: ")
    dir = input()

    while (not os.path.isdir(dir)):
        print("Ne postoji uneti direktorijum")
        dir = input()

    parser1 = Parser()
    root = Trie()
    links = []
    start = time.time()
    g = Graph()
    for dirpath, dirnames, files in os.walk(str(dir)):
        print(f'Found directory: {dirpath}')
        for fn in files:
            if str(dirpath + '//' + fn).endswith('.html'):
                parser1.parse(dirpath + '//' + fn)
                print('parsiram:   ' + dirpath + '//' + fn)
                for word in parser1.words:
                    root.insert(word,os.path.join(dirpath,fn))

    print(root.search("python"))
    end = time.time()
    print(end - start)
    #ucitajUGraf(str(dir))

    s = ParsirajU(root)
    if(s.Duzina() == 0):
        print("Rezultat pretrage : 0")
    else:
        print("Rezultat pretrage : ")
        s.Ispisi()