import math
class Ispis:

    def __init__(self,r1,r2,r3,r4,link):
        self.link = link
        self.rang1 = r1
        self.rang2 = r2
        self.rang3 = r3
        self.rang4 = r4

    def Ispisi(self):
        m1 = round(self.rang1,3)
        m2 = round(self.rang2,3)
        m3 = round(self.rang3,3)
        m4 = round(self.rang4,3)
        print(f'{m1:2}  {m2:6}  {m3:6}  {m4:6} ',self.link)