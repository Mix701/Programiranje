a = input("Unesite broj sekundi(max 86400, min 0): ")
a = int(a)
b = a

if a < 0 or a > 86400:
    print("Netacan broj sekundi u jednom danu!")
else:

        hh = a // 3600
        a = a - (hh * 3600)
        mm = a // 60
        a = a - (mm*60)
        ss = a
        print(str(b) + " sekundi predtsatvlja " + str(hh) + " sati " + str(mm) + " minuta i " + str(ss) + " sekundi")