import os

from TrieStruct import Trie
from parser2 import Parser
class GraphVertex:
    def __init__(self,naziv,links,words):

        self.naziv = naziv #link stranice
        self.links = links
        self.words = words
        self._trie = self.tri()
        self.pokazivanja = set() #cvorovi koji pokazuju na taj cvor

        #self.tri()

    def parser(self):
        parser = Parser()
        #print(self.naziv)
        return parser.parse(self.naziv)

    def tri(self):
        x = Trie()
        for i in range(len(self.words)):
            x.insert(self.words[i],i)
        return x

    def getTrie(self):
        return self._trie

    #def __hash__(self):
     #   return hash(id(self))

class GraphEdge:
    def __init__(self,polazni,dolazni):
        self.polazni = polazni #naziv cvora koji se koristi samo kao imena
        self.dolazni = dolazni #naziv ciljnog cvora

    def __hash__(self):
        return hash((self.polazni, self.dolazni))

class Graph:
    def __init__(self):

        self.lista_cvorova = dict()
        self.lista_grana = []
        self.sveReci = set() #sve rijeci bez duplikata

    def dodajCvor(self,naziv_cvora,links,words,path): #naziv cvora je link na kom se cvor nalazi valjda

        if naziv_cvora not in self.lista_cvorova:
            #print(naziv_cvora)
            cvor = GraphVertex(naziv_cvora,links,words)
            self.sveReci = self.sveReci.union(set(cvor.words))
            self.lista_cvorova[naziv_cvora] = cvor  #dodavanje novog cvora u graf
        for link in self.lista_cvorova[naziv_cvora].links:
            if link in self.lista_cvorova:
                self.lista_cvorova[link].pokazivanja.add(naziv_cvora)
            else:
                parser = Parser()
                full_path = os.path.join(path,link)
                linkovi,reci = parser.parse(full_path)
                c = GraphVertex(link,linkovi,reci)
                self.lista_cvorova[link] = c

                self.lista_cvorova[link].pokazivanja.add(naziv_cvora)

            grana = GraphEdge(naziv_cvora,link)
            self.lista_grana.append(grana)


