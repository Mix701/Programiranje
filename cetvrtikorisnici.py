s = open('korisnici.txt', 'r')

lista = s.readlines()
i=0
l=0
for item in lista:
    j=0
    for item in lista[i]:
        l+=1
        j+=1
        if item == "|":
          g = j
    print("Korisnicko ime je:" + lista[i][0:g-1])
    print("Lozinka je:" + lista[i][g:l])

    i+=1

    s.close()
