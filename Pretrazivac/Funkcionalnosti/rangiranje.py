import os
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
    return rjecnik,recnikZaRazliciteReci


def uticajVrednostiLinkova(root, linkoviUpita, rjecnikUpita):
    # linkovi upita su kratki kao i rjecnikUpita

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

        for link2 in root.get_incoming(link1):
            if link2 in rjecnikUpita.keys():
                dodatak += rjecnikUpita[link2]
                rjecnikUpita[link1] = dodatak * 0.3
    return rjecnikUpita

def  uticajBrojaLinkova(root,g,rjecnikLinkova,rijeci):

        for page in rjecnikLinkova.keys():
            for node in g.get_incoming(os.path.abspath(page)):
                if root.zaVrednost(node):
                    rjecnikLinkova[page]+=1
                else:
                    rjecnikLinkova[page]+=0.5
        return rjecnikLinkova

def uticajRazlicitihReci(mapaRazlicitihReci,mapaZaRang):
        for page in mapaZaRang.keys():
            mapaZaRang[page]=mapaRazlicitihReci[page]*mapaZaRang[page]
        return mapaZaRang


def uticajBrojaReci(mapaZaRang):
    for page in mapaZaRang.keys():
        mapaZaRang[page] = mapaZaRang[page]*0.5
    return mapaZaRang



