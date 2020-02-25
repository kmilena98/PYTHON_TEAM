import os
from StrukturePodataka.graf import Graph

class RezultatParsirajna:
    def __init__(self, links, words, name, abs_path):
        for i in range(len(links)):
            links[i] = os.path.relpath(links[i], abs_path)
        self.links = links
        self.words = words
        self.name = name
        self.googleRang = 0
        self.mapForH = {}  # this is map/dict for matrixH (google rank)
        self.mapaPokazivacaNaFajl = {}
        for link in self.links:
            self.mapForH[link] = 0  # inicijalizujemo recnik
        self.rang = 0
