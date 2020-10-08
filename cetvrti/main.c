#include <stdio.h>
#include <stdlib.h>

int main()
{
   int niz[5];

   int* p=niz;
   int i;
   int a=0;
   for(i=0;i<5;i++){
    printf("Unesite %d. broj\n", i+1);
    scanf("%d", p+i);

   }

    for(i=0;i<5;i++){
       if((p+i)>a){
        a=*(p+i);
       }
    }

printf("Najveci clan je:%d\n", a);






    return 0;
}
