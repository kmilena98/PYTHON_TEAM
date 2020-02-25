import  os
class Set():
    def __init__(self,skup = None):
        if skup==None:
            self.dict = {}
        else:
            self.dict = skup.dict

    def dodaj(self, Link):
        if not self.sadrziLink(Link):
            self.dict[Link] = Link

    def kljucevi(self):
        return self.dict.keys()

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
        ret = Set()
        for link1 in s2.dict:
            ret.dodaj(link1)
        for link2 in self.dict:
            ret.dodaj(link2)
        return ret

    def Presek(self, s2):
        ret= Set()
        for Link in self.dict:
            if s2.sadrziLink(Link):
                ret.dodaj(Link)
        return ret

    def Komplement(self, s2):
        ret = Set()
        for Link in self.dict:
            if not s2.sadrziLink(Link):
                ret.dodaj(Link)
        return ret

    def Ispisi(self):
        lista = []
        for item in self.dict:
            print(item)


    def toList(self):
        ret = []
        for item in self.dict.keys():
            ret.append(item)
        return ret