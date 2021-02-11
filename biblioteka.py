class knjiga:
    def __init__(self, isbn, naslov, autor, zarn):
        self.isbn = isbn
        self.naslov = naslov
        self.autor = autor
        self.zarn = zarn

    def unosKnjige(self, isbn):
        self.isbn = isbn
        self.naslov = input("Unesite naslov knjige: ")
        self.autor = input("Unesite autora: ")
        self.zarn = input("Unesite zanr: ")

    def podaciKnjiga(self):
        print(self.isbn)
        print(self.naslov)
        print(self.autor)
        print(self.zarn)

class biblioteka:
    def __init__(self, naziv):
        self.naziv = naziv
        self.knjige = []

    def kreiranjeBiblioteke(self):
        self.naziv = input("Unesite naziv biblioteke: ")
        print("Biblioteka je uspesno kreirana!")

    def dodavanjeKnjige(self, isbn, naslov, autor, zarn):
        self.knjige.append({"isbn": isbn, "Naslov": naslov, "Autor": autor, "Zarn": zarn})

    def podaciBiblioteka(self):
        print("Naziv biblioteke: ", self.naziv)
        #print(self.knjige)
        n = ""
        i = 0
        k = knjiga(i, n, n, n)
        for k in self.knjige:
                print(k)

    def pronadjiKnjigu(self):
        n = ""
        i = 0
        k = knjiga(i, n, n, n)
        id = int(input("Unesite id knjige: "))
        for k in self.knjige:
            if id == k["isbn"]:
                print(k)
                break
        print("Ne postoji knjiga sa unetim id u biblioteci!")

    def provera(self):
        n = ""
        i = 0
        k = knjiga(i, n, n, n)
        exist = False
        m = 0
        while exist == False:
            m = 0
            id = int(input("Unesite id knjige: "))
            for k in self.knjige:
                if id == k["isbn"]:
                    print("Vec postoji knjiga sa unetim id u biblioteci!")
                    m = 1
            if m == 0:
                exist = True
                return id


if __name__ == '__main__':

    postojiBiblioteka = False
    n = ""
    i = 0
    b = biblioteka(n)
    k = knjiga(i, n, n, n)

    while True:
        print("BIBLIOTEKA")
        print("1. Dodajte biblioteku: ")
        print("2. Dodakte knjigu u biblioteku:")
        print("3. Izlistajte podatake o biblioteci:")
        print("4. Izlistajte podatake o knjizi:")
        print("5 - Izalaz")
        a = input("Vas izbor: ")
        if a == '1':
            if postojiBiblioteka == False:
                b.kreiranjeBiblioteke()
                postojiBiblioteka = True
            else:
                print("Vec ste uneli biblioteku!")
        elif a  == '2':
            if postojiBiblioteka == True:
                f = b.provera()
                k.unosKnjige(f)
                b.dodavanjeKnjige(f,  k.naslov, k.autor, k.zarn)
            else:
                print("Morate prvo kreirati bibloteku!")
        elif a == '3':
            if postojiBiblioteka == True:
                b.podaciBiblioteka()
            else:
                print("Morate prvo kreirati bibloteku!")
        elif a == '4':
            if postojiBiblioteka == True:
                b.pronadjiKnjigu()
            else:
                print("Morate prvo kreirati bibloteku!")
        elif a == '5':
            break
        else:
            print("Uneliste nevalidnu opciju")