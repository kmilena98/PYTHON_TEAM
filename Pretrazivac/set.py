class Set():
    def __init__(self):
        self.dict = {}

    def dodaj(self, Link):
        if not self.sadrziLink(Link):
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
                rezultat.dodaj(Link)
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
            if s1.dict.__contains__(Link):
                s1.UkloniLink(Link)
        return s1

    def Ispisi(self):
        for item in self.dict:
            print(item)