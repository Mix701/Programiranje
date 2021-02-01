import math
pi = math.pi
class krug:
    def __init__(self,r, o, p):
        self.r = r
        self.o = o
        self.p = p

    def oKruga(self):
        self.o= round(2 * self.r * pi, 2)
        print("Obim kruga je: " + str(self.o))

    def pKruga(self):
        self.p = round(self.r ** 2 * pi, 2)
        print("Povrsina kruga je: " + str(self.p))

class kvadrat:
    def __init__(self, a, o, p):
        self.a = a
        self.o = o
        self.p = p

    def oKvadrata(self):
        self.obim = 4 * self.a
        print("Obim kvadrata je: " + str(self.obim))

    def pKvadrata(self):
       self.p = self.a ** 2
       print("Povrsina kvadrata je: " + str(self.p))

class pravougaonik:
    def __init__(self, a, b, o, p):
        self.a = a
        self.b = b
        self.o = o
        self.p = p

    def oPravougaonika(self):
        self.o = 2 * self.a + 2 * self.b
        print("Obim pravougaonika je: " + str(self.o))

    def pPravougaonika(self):
        self.p = self.a * self.b
        print("Povrsina pravougaonika je: " + str(self.p))

if __name__ == '__main__':
    while True:
        print("KLIKNITE :")
        print("1. Ako zelite da program izracuna obim i povrsinu kruga.")
        print("2. Ako zelite da program izracuna obim i povrsina kvadrata.")
        print("3. Ako zelite da program izracuna obim i povrsin pravougaonika.")
        print("4. Ako zelite da napustite program ")
        izbor = input("Vas izbor: ")
        if izbor == '1':
            o = 0
            p = 0
            r = float(input("Unesite poluprecinik kruga: "))
            kr = krug(r, o, p)
            kr.oKruga()
            kr.pKruga()
        elif izbor == '2':
            o = 0
            p = 0
            a = int(input("Unesite stranicu kvadrata: "))
            kv = kvadrat(a, o, p)
            kv.oKvadrata()
            kv.pKvadrata()
        elif izbor == '3':
            o = 0
            p = 0
            a = int(input("Unesite prvu stranicu pavougaonika: "))
            b = int(input("Unesite drugu stranicu pavougaonika: "))
            p = pravougaonik(a, b, o, p)
            p.oPravougaonika()
            p.pPravougaonika()
        elif izbor == '4':
            break
        else:
            print("Uneliste nevaldnu opciju!")