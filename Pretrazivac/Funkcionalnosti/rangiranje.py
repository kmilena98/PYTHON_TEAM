import os
import math
class PageRang:

    def __init__(self,page,rang):
        self.page = page
        self.rang = rang

    def getPage(self):
        return self.page
    def getRang(self):
        return self.rang

    def setPage(self,p):
        self.page = p
    def setRang(self,r):
        self.rang = r


def rjecnikZaRang(root, d, s):
    rjecnik = {}
    recnikZaRazliciteReci = {}
    delovi = []
    for a in d:
        if a.upper() not in ("NOT","AND","OR"):
            delovi.append(a)

    novaLista = []  # ulisti se nalaze linkovi
    for a in s.kljucevi():
        # print(a)
        m = os.path.relpath(a)
        novaLista.append(os.path.abspath(a))

    for page in novaLista:
        rjecnik[page] = 0  # inicijalizovanje svih vrednosti rjecnika
        recnikZaRazliciteReci[page]=0


    for rec in delovi:
        vrednost = root.zaVrednost(rec)  # vrednost treba da bude cvor na kom  se zavrsava rijec
        novaMapa = {}
        for pom in vrednost[1].links:
            m = os.path.relpath(pom)
            novaMapa[os.path.abspath(pom)]=vrednost[1].links[pom]

        if vrednost[1]:  # da li je ovde vrednost[1] ili vrednost od 0 ja msm od 0!!
            for page in novaMapa:
                if page in rjecnik.keys():
                    rjecnik[page] += novaMapa[page]
                    recnikZaRazliciteReci[page]+=1

    #for page in rjecnik.keys():
    #   rjecnik[page] = rjecnik[page]*0.5
    return rjecnik,recnikZaRazliciteReci#rjecnik je pravi rjecnik sa brojem reci a recnik za razlicite reci je br razlicitih reci na linku


def uticajVrednostiLinkova(root, linkoviUpita, rjecnikUpita):
    # linkovi upita su kratki kao i rjecnikUpita
    broj = 10 * 0.5
    for link1 in linkoviUpita:
        rjecnikUpita[link1] = broj

    for link1 in linkoviUpita:
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

        
        pomList = []
        for a in rjecnikUpita.keys():
           m = os.path.relpath(a)
           pomList.append(os.path.abspath(m))
        '''


        dodatak = 1
        for link2 in root.get_incoming(link1):
            if link2 in rjecnikUpita.keys():
                dodatak += rjecnikUpita[link2] #dodatak sadrzi zbir vrednosti svih njegovih linkova
        rjecnikUpita[link1] = broj/dodatak

    #print(rjecnikUpita)

    return rjecnikUpita

def  uticajBrojaLinkova(root,g,rjecnikLinkova,rijeci):

        broj = 10*0.2
        for page in rjecnikLinkova.keys():
            rjecnikLinkova[page]=1

        for page in rjecnikLinkova.keys():
            for node in g.get_incoming(os.path.abspath(page)):
                if root.zaVrednost(node):
                    rjecnikLinkova[page]+=1
                else:
                    rjecnikLinkova[page]+=0

        #print(rjecnikLinkova)

        for page in rjecnikLinkova.keys():
            rjecnikLinkova[page] = broj/rjecnikLinkova[page]
        #print(rjecnikLinkova)
        return rjecnikLinkova

def uticajRazlicitihReci(mapaRazlicitihReci,mapaZaRang):
    rang1 = {}
    for page in mapaZaRang.keys():
        rang1[page] = 10

    for page in mapaZaRang.keys():
        rang1[page]= math.pow(rang1[page],mapaRazlicitihReci[page])
    return rang1


def uticajBrojaReci(mapaZaRang):
    broj = 10*0.3
    for page in mapaZaRang.keys():
        mapaZaRang[page] = broj/mapaZaRang[page]
    return mapaZaRang




