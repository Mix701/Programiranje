#include <stdio.h>
#include <stdlib.h>
#include "F.h"
int main()
{
    int n, m, reci;
    char a[] = "DAT1.txt";
    char b[] = "DAT2.txt";
    char kontejner[50];
    char sadrzaj [50];
    char najduze [20];
    FILE* f = fopen(a, "w+");
        UnosSadrzaja(f, sadrzaj);
        fseek(f, 0, SEEK_SET);
        UzimanjeSadrzaja(kontejner, f);
        BrojanjeReci(kontejner, &reci);
       fclose(f);
      FILE* s = fopen(b, "w+");
        PopunjavanjeDruge(s, reci);
        fclose(s);
    return 0;
}
