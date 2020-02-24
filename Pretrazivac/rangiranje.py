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


def rjecnikZaRang(root, delovi, s):
    rjecnik = {}

    novaLista = []  # ulisti se nalaze linkovi

    for a in s.kljucevi():
        # print(a)
        novaLista.append(a)
    # listalinkova = [k for k in s]   #ovako se smestaju kljucevi iz recnika u listu
    # print("LISTA :")
    # print(listaLinkova)

    for page in novaLista:
        # print(page)
        rjecnik[page] = 0  # inicijalizovanje svih vrednosti rjecnika
        # print("ulazi u 2 for")

    for rec in delovi:
        vrednost = root.zaVrednost(rec)  # vrednost treba da bude cvor na kom  se zavrsava rijec
        if vrednost[0]:
            print("Linkovi cvora:")
            print(vrednost[1].links)

        if vrednost[1]:  # da li je ovde vrednost[1] ili vrednost od 0 ja msm od 0!!
            for page in vrednost[1].links:
                if page in rjecnik.keys():
                    rjecnik[page] += vrednost[1].links[page]

    for page in novaLista:
       rjecnik[page] = rjecnik[page] * 0.5

    return rjecnik


def uticajVrednostiLinkova(root, linkoviUpita, rjecnikUpita):
    # linkovi upita su kratki kao i rjecnikUpita
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
                rjecnikUpita[os.path.relpath(link1)] = dodatak * 0.3

def  uticajBrojaLinkova(root,g,rjecnikLinkova,rijeci):

        for page in rjecnikLinkova.keys():
            for node in g.get_incoming(os.path.abspath(page)):
                if root.zaVrednost(node):
                    rjecnikLinkova[page]+=1
                else:
                    rjecnikLinkova[page]+=0.5

        return rjecnikLinkova



