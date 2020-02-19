from TrieStruct import *
from parser2 import Parser
from InputParser import ParsirajU
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
    links = []
    start = time.time()
    for dirpath, dirnames, files in os.walk(str(dir)):
        print(f'Found directory: {dirpath}')
        for fn in files:
            if str(dirpath + '\\' + fn).endswith('.html'):
                parser1.parse(dirpath + '\\' + fn)
                print('parsiram:   ' + dirpath + '\\' + fn)
                for word in parser1.words:
                    root.insert(word,fn)

    print(root.search("python"))
    end = time.time()
    print(end - start)
    ParsirajU()