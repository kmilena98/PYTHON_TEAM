from StrukturePodataka.set import *
from StrukturePodataka.TrieStruct import *
from StrukturePodataka.graf import *
import os
def ParsirajU(trie):
    upit = input("Unesite upit:")
    delovi = upit.split()
    rez = [None]*len(delovi)

    if len(delovi) == 0:
        ParsirajU(trie)
    elif len(delovi) > 3:
        for rec in delovi:
             if rec.upper() in ("AND", "OR", "NOT"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
                ParsirajU(trie)
    else:
        if delovi[0].upper() in ("AND", "OR") or delovi[-1].upper() in ("AND", "OR", "NOT"):
            print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
            ParsirajU(trie)

    i = 0
    #trazenaLista = Set()
    for rec in delovi:
        if rec.upper() in ("AND", "OR", "NOT"):
            rez[i] = rec.upper()
            i = i + 1
        else:
            if not trie.search(rec):
                rez[i] = Set()
                i = i + 1
            else:
                rez[i] = trie.search(rec)[2].IntoSet() #dobijamo linkove na koje pokazuje taj cvor ili reci AND OR I NOT
                #trazenaLista[i] = root.search(rec)[2].IntoSet()
                i = i + 1

    s = Set()
    i = 0
    while i < len(rez):
        if rez[i] == "AND":
            s = s.Presek(rez[i+1])
            i = i + 2
        elif rez[i] == "NOT":
            s = s.Komplement(rez[i+1])
            i = i + 2
        elif rez[i] == "OR":
            s = s.Unija(rez[i+1])
            i = i + 2
        else:
            s = s.Unija(rez[i])
            i = i + 1
    return s,delovi
#s je rezultat upita







