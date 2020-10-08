#include <stdio.h>
#include <stdlib.h>
#include <string.h>

    int nalazak(char *s1,char a){
        int i,j=0;
        for(i=0;i<strlen(s1);i++){
            if(s1[i]==a){
                j++;
            }
        }
        return j;
    }

int main()
{
    char s1[100];
    printf("unesite string \n");
    gets(s1);
    char a;
    printf("Unesite sta se trazi \n");
    scanf("%c",&a);
    int b;
    b=nalazak(s1,a);
    printf("Nalazi se %d puta \n",b);
    return 0;
}
