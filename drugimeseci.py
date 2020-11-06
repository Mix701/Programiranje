a = input("Unesite mesec u godini: ")
a = int(a)
if a<1 or a>12:
    print("Uneti mesec ne postoji!")
else:
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        print("Uneti mesec ima 31 dan.")
    elif a == 4 or a == 6 or a == 9 or a == 11:
        print("Uneti mesec ima 30 dana.")
    elif a == 2:
        print("Uneti mesec ima 28 dana.")