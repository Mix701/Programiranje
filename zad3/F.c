#include <stdio.h>
#include <stdlib.h>
#include "imenaF.h"
void UnosDuzineImena(int* n){
printf("\nUnesite duzinu imena vase datoteke:");
scanf("%d", n);
fflush(stdin);
}
void UnosImena(int n, char* ime){
printf("\nUnesite ime vase datoteke (molio bih Vas da unesete ime duzine koju ste zadali, u suprotnom Vasa datoteka nece biti kreirana):");
gets(ime);
    ime[n] = '.';
    ime[n+1] = 't';
    ime[n+2] = 'x';
    ime [n+3] = 't';
    ime [n+4] = '\0';
}
void KreiranjeDatoteke(char* ime, FILE* f){
f = fopen(ime, "w+");
if(f==NULL){
    printf("\nKreiranje datoteke neuspesno.");
}else{
printf("\nKreiranje uspesno.");
}
}
void UnosSadrzaja(FILE* f, char* sadrzaj){
printf("\nUnesite zeljeni sadrzaj u datoteku:");
gets(sadrzaj);
fflush(stdin);
if(fputs(sadrzaj, f)==EOF){
    printf("\nNeuspesno popunjavanje datoteke");
}else{
printf("\nUspesno popunjavanje datoteke ");
}
fflush(stdout);
}
void UzimanjeSadrzaja(char* kontejner, FILE* f){
fgets(kontejner, 50, f);
}
void BrojanjeReci(char* kontejner, int* reci){
int i, p=0;
for(i=0; i<50; i++){
    if(kontejner[i]==32){
        p++;
    }
}
*reci = p+1;
puts(kontejner);
}
void PopunjavanjeDruge(FILE* f, int reci){
fprintf(f, "Broj reci u datoteci je %d.", reci);
}
void ZatvaranjeDatoteke(FILE* f){
fclose(f);
}
void NajduzaRec(char* kontejner, char* najduze){
    int max=0;
    int k=0, s;
    int i,j, p;
for(i=0; i<50; i++){
if(kontejner[i]==32){
    printf("\n %d ", k);
    j=i;
    goto labela;
}
if (kontejner[i]==13){
goto labela2;
}
    k++;
    labela:
if(k>=max){
        max=k;
if(k==i){
    p=j-k;
}else{
    p=j-k+1;
}
for(s=0; s<k; s++){
    najduze[s]=kontejner[p];
    p++;
}
    printf("\n");
    puts(najduze);
}
k=0;
}
    labela2:
    printf("\nNajduza rec je: ");
    puts(najduze);
}
