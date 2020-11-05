a = input("Unesite broj: ")
a = int(a)
proizvod=1
for i in range(1, a+1):
proizvod=proizvod*i
print("Faktorijel  broja je: " + str(proizvod))