from TrieStruct import TrieNode
from parser import Parser
import os

if __name__ == "__main__":
    print("Trenutni direktorijum je: " + os.getcwd())
    print("Unesite direktorijum koji zelite da parsirate: ")
    dir = input()

    parser1 = Parser()
    root = TrieNode(None)

    for dirpath, dirnames, files in os.walk(str(dir)):
        if not dirpath:
            print("Ne posotji takav direktorijum!")
            break
        else:
            print(f'Found directory: {dirpath}')
        for fn in files:
            if str(dirpath + '\\' + fn).endswith('.html'):
                parser1.parse(dirpath + '\\' + fn)
                print('parsiram:   ' + dirpath + '\\' + fn)
                for word in parser1.words:
                    root.add(word, fn)


    print(root.findWord("ej"))