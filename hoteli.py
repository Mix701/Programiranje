hoteli = [
    {"Naziv": "Sheraton", "Broj zvezdica": "4", "Adresa": "Polgar Andraša 1", "Grad": "Novi Sad"},
    {"Naziv": "Vojvodina", "Broj zvezdica": "3", "Adresa": "Trg Slobode 2", "Grad": "Novi Sad"},
]


class Smestaj:
    def __init__(self, naziv, adresa, grad):
        self.ime = naziv
        self.adresa = adresa
        self.grad = grad

    def __str__(self):
        return f"Naziv: {self.ime}, Adresa: {self.adresa}, Grad: {self.grad}"


class Hotel(Smestaj):
    def __init__(self, br_zvezdica):
        Smestaj.__init__(self)
        self.br_zvezdica = broj_zvezdica

    def __str__(self):
        return f"Naziv: {self.ime}, Adresa: {self.adresa}, Grad: {self.grad}, Broj Zvezdica: {self.br_zvezdica}"

    def kreiraj_hotel(self):
        self.ime = input("Unesite naziv hotela: ")
        self.br_zvezdica = input("Unesite broj zvezdica hotela: ")
        self.adresa = input("Unesite adresu u gradu  gde se hotel nalazi: ")
        self.grad = input("Unesite grad gde se hotel nalazi: ")
        hoteli.append({"Naziv": self.ime, "Broj zvezdica": self.br_zvezdica, "Adresa": self.adresa,
                       "Grad": self.grad})


if __name__ == '__main__':
    izbor = '1'
    while izbor != '0':
        izbor = input(
            "Unesite: \n"
            " 1 za kreiranje novog hotela \n"
            " 2 za ispis svih kreiranih hotela \n"
            " 0 da završite program \n ")
        if izbor == '1':
            a = Hotel
            Hotel.kreiraj_hotel(a)
            print("Hotel je uspešno dodat!", end='\n')

        elif izbor == '2':
            i = 0
            for a in hoteli:
                print(hoteli[i], end='\n')
                i = i+1

        elif izbor == '0':
            break

        else:
            print("Vas unos nije validan unesite nesto validno.")