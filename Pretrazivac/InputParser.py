from set import *
from TrieStruct import *
def ParsirajU(root):
    upit = input("Unesite upit:")
    delovi = upit.split()
    skup = [None]*len(delovi)


    i = 0
    for rec in delovi:
        if rec.upper() in ("AND", "OR", "NOT"):
            skup[i] = rec.upper()
            print(rec.upper())
            i += 1
        else:
            if not root.search(rec)[0][0] :
                skup[i] = Set()
                print("Rec " + rec + " ne postoji u parsiranim fajlovima")
                i+=1
            else:
                skup[i] = root.search(rec)[2].IntoSet()
                skup[i].Ispisi()
                i+=1

    if len(delovi) > 3:
        for rec in delovi:
             if rec.upper() in ("AND", "OR", "NOT"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
                ParsirajU(root)

    if delovi[0].upper() in ("AND", "OR") or delovi[-1].upper() in ("AND", "OR", "NOT"):
        print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
        ParsirajU(root)





