#include <stdio.h>
#include <stdlib.h>
int deljiv(int* a){
    int i=0;
    int j=0;
    for(i=0;i<5;i++){
        if(*(a+i)%3==0){
            j++;
        }}
        return j;

}
int main()
{
    int niz [5];
    int i;
    printf("Unesite elemente niza: \n ");
    for(i=0;i<5;i++){
        scanf("%d",&niz[i]);
    }
    int* a= niz;
    int j= deljiv(a);
    printf("%d",j);
    return 0;
}
