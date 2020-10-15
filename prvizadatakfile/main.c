#include <stdio.h>
#include <stdlib.h>

int main()
{
FILE* f= fopen("FAJL.txt", "w");
printf("Unesite tekst :");
char tekst[100];
gets(tekst);
fputs(tekst, f);
printf("\nUnesite sta zelite da se prebroji:");
char karakter;
scanf("%c", &karakter);
fgets(tekst, 0, f);
fseek(f, 0, SEEK_SET);
int k=0;
for(int i=0; i<100; i++){
    if(karakter==tekst[i])
      k++;
}
fclose(f);
printf("Znak se pojavio %d puta.", k);

    return 0;
}
