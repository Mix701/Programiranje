import uuid

list_voca_u_skladistu = []


class Voce:
    def __init__(self, naziv, tip_voca):
        self.naziv = naziv
        self.tip_voca = tip_voca
        self.voce_id = str(uuid.uuid4().hex)
        self.korpa = []

    def __str__(self):
        return f"Lista voca u skladištu: {print(list_voca_u_skladistu)}"


class Korpa:
    def __init__(self):
        self.korpa_id = str(uuid.uuid4().hex)
        self.voce = []
        self.broj_jabuka = '0'
        self.broj_visanja = '0'
        self.broj_malina = '0'

    def __str__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


if __name__ == '__main__':
    print("Pristisnite: ", end='\n')
    print("1. za Kreiranje korpe")
    print("2. za Kreiranje voća")
    print("3.  zaIspis voća koje postoje u sistemu")
    print("4. za Dodavanje postojećeg voća u korpu")
    print('5. za Brisanje voća iz korpe')
    print("6. za Ispis sadržaja korpe")
    print("7. za Ispis voća po tipu u korpi")
    print("0. za Kraj programa")
    izbor = '1'
    while izbor != '0':
        izbor = input("Unesite vas izbor: ")
        if izbor == '1':
            nova_korpa = Korpa()
            print("Nova korpa je uspešno dodata!")
        elif izbor == '2':
            tip = input("Unesite tip voća (jabuka, visnja, malina): ")
            naziv = input("Unesite naziv voćke: ")
            nova_vocka = Voce(naziv, tip)
            list_voca_u_skladistu.append({"Tip": nova_vocka.tip_voca, "Naziv": nova_vocka.naziv, "Id": nova_vocka.voce_id})
            print("Voćka je uspešno dodata!")
        elif izbor == '3':
            nesto = Voce
            nesto.__str__(nesto)
        elif izbor == '4':
            id = input("Unesite id vocke koju zelite da dodate u korpu: ")
            for vocka in list_voca_u_skladistu:
                if id == list_voca_u_skladistu[vocka.values(2)]:
                    vocka_za_korpu = list_voca_u_skladistu[vocka]
                    print(nova_korpa + vocka_za_korpu)
                else:
                    print("U skladistu ne postoji voćka sa takvim ID-om.")

        elif izbor == '5':
            pass
        elif izbor == '6':
            pass
        elif izbor == '7':
            pass
        elif izbor == '0':
            print("Doviđenja!")
            break
        else:
            print("Uneli ste nevalidan izbor!")