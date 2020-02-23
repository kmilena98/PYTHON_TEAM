from set import *
from TrieStruct import *
from graf import *
import os
def ParsirajU(root):
    upit = input("Unesite upit:")
    delovi = upit.split()
    rez = [None]*len(delovi)

    if len(delovi) == 0:
        ParsirajU(root)
    elif len(delovi) > 3:
        for rec in delovi:
             if rec.upper() in ("AND", "OR", "NOT"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
                ParsirajU(root)
    else:
        if delovi[0].upper() in ("AND", "OR") or delovi[-1].upper() in ("AND", "OR", "NOT"):
            print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
            ParsirajU(root)

    i = 0
    #trazenaLista = Set()
    for rec in delovi:
        if rec.upper() in ("AND", "OR", "NOT"):
            rez[i] = rec.upper()
            i = i + 1
        else:
            if not root.search(rec)[0][0]:
                rez[i] = Set()
                i = i + 1
            else:
                rez[i] = root.search(rec)[2].IntoSet() #dobijamo linkove na koje pokazuje taj cvor ili reci AND OR I NOT
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

def rjecnikZaRang(root,delovi,s):

    rjecnik = {}

    novaLista = []# ulisti se nalaze linkovi

    for a in s.kljucevi():
        #print(a)
        novaLista.append(a)
    #listalinkova = [k for k in s]   #ovako se smestaju kljucevi iz recnika u listu
    #print("LISTA :")
    #print(listaLinkova)

    for page in novaLista:
        #print(page)
        rjecnik[page] = 0 #inicijalizovanje svih vrednosti rjecnika
        #print("ulazi u 2 for")

    for rec in delovi:
        vrednost = root.zaVrednost(rec) #vrednost treba da bude cvor na kom  se zavrsava rijec
        if vrednost[0]:
            print("Linkovi cvora:")
            print(vrednost[1].links)

        if vrednost[1]: #da li je ovde vrednost[1] ili vrednost od 0 ja msm od 0!!
            for page in vrednost[1].links:
                if page in rjecnik.keys():
                    rjecnik[page]+=vrednost[1].links[page]

    for page in novaLista:
        rjecnik[page]= rjecnik[page]*0.5

    return rjecnik

def uticajLinkova(root,linkoviUpita,rjecnikUpita):
        #linkovi upita su kratki kao i rjecnikUpita
    for link1 in linkoviUpita.kljucevi():
        # I link1 je kratak takodje
        dodatak = 0


        link1 = os.path.abspath(link1)
        '''
        #print("ONI KOJI POKAZUJU NA CVOR INDEX")
        #print(root.get_incoming(link1))
        
        novaLista1 = []
        for lik1 in root.get_incoming(link1):
            novaLista1.append(os.path.abspath(lik1))
            
        novaLista2 =[]
        for lik2 in rjecnikUpita.keys():
            novaLista2.append(os.path.abspath(lik2))
        
        '''
        for link2 in root.get_incoming(link1):
            if os.path.relpath(link2) in rjecnikUpita.keys():
                dodatak += rjecnikUpita[os.path.relpath(link2)]
                rjecnikUpita[os.path.relpath(link1)]= dodatak*0.3










