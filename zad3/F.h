
#ifndef IMENAF_H_INCLUDED
#define IMENAF_H_INCLUDED
void UnosDuzineImena(int* n);
void UnosImena(int n, char* ime);
void KreiranjeDatoteke(char* ime, FILE* f);
void UnosSadrzaja(FILE* f, char* sadrzaj);
void UzimanjeSadrzaja(char* kontejner, FILE* f);
void BrojanjeReci(char* kontejner, int* reci);
void PopunjavanjeDruge(FILE* f, int p);
void ZatvaranjeDatoteke(FILE* f);
void NajduzaRec(char* kontejner, char* najduze);
#endif // IMENAF_H_INCLUDED
