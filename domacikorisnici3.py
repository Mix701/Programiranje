def Meni():
    print("------------------RESTART-----------------")

hleb = True
s = open('korisnici.txt', 'w')
while hleb:
    m = input("Korisnicko ime: ")
    n = input("Lozinka: ")
    s.write(m)
    s.write(" | ")
    s.write(n)
    s.write("\n")
    Meni()
    k = input("Da li zelite da nastavite")
    if k == 'da':
        hleb = True
    else:
        hleb = False
s.close()