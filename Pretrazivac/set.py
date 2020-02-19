class Set():
    def __init__(self):
        self.dict = {}

    def dodaj(self, Link):
        if not self.contains(Link):
            self.dict[Link] = Link

    def sadrziLink(self, Link):
        for i in self.dict:
            if i == Link:
                return True
        return False

    def Duzina(self):
        return len(self.dict)

    def UkloniLink(self, Link):
        del self.dict[Link]

    def Unija(self, s2):
        import copy
        rezultat = copy.copy(self)
        if s2 is not None:
            for Link in s2.dict:
                rezultat.add(Link)
        return rezultat

    def Presek(self, s2):
        rezultat = Set()
        for Link in self.dict:
            for Link2 in s2.dict:
                if Link == Link2:
                    rezultat.add(Link)
        return rezultat

    def Komplement(self, s2):
        import copy
        s1 = copy.copy(self)
        for Link in s2.dict:
            if s1.contains(Link):
                s1.remove(Link)
        return s1

def listIntoSet(lista): #pretvara listu u set, koristi se u parseruUpita
    s = Set()
    for Link in lista:
        s.add(Link)
    return s