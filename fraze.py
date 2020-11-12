def Unos():
    m = input("Unesite zeljenu frazu:")
    return m

def BrojReci(n):
    m = set()
    j=0
    i=0
    print(n[i].capitalize(), end=" ")


    for item in n:

        if item == ' ':
            print(n[i+1].capitalize(), end=" ")
        i+=1
    return m

n = Unos()


BrojReci(n)