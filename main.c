#include <stdio.h>
#include <stdlib.h>
void UnosImenaDatoteka(char* prva, int n){
printf("\nUnesite naziv datoteke:");
gets(prva);
prva[n]='.';
prva[n+1]='t';
prva[n+2]='x';
prva[n+3]='t';
prva[n+4] = '\0';
}
void DuzinaNazivaDatoteke(int* n){
printf("\nUnesite duzinu naziva vase datoetke:");
scanf("%d", n);
fflush(stdin);
}
void PopunjavanjeDatoteke(char* tekst, FILE* f){
printf("\nPopunite vasu datoteku:");
fflush(stdin);
gets(tekst);
fputs(tekst, f);
}
int main()
{
int A, B;
char tekst[100];
char tekst1[100];
DuzinaNazivaDatoteke(&A);
char* prva = malloc(A*sizeof(char)+5);
UnosImenaDatoteka(prva, A);
FILE* f = fopen(prva, "w+");
PopunjavanjeDatoteke(tekst, f);
fclose(f);
DuzinaNazivaDatoteke(&B);
char* druga = malloc(A*sizeof(char)+5);
UnosImenaDatoteka(druga, B);
FILE* g = fopen(druga, "w+");
PopunjavanjeDatoteke(tekst1, g);
fclose(g);
FILE* p = fopen("izlaz.txt", "w+");
fputs(tekst, p);
fseek(p, 0, SEEK_CUR);
fputs(tekst1, p);
fclose(p);
    return 0;
}
