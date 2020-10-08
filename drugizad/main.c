#include <stdio.h>
#include <stdlib.h>
#include<string.h>
int jednaki(char* a1, char* b2){
    int i;
    if(a1==b2){
        i=0;
    }else{
    i=1;
    }

    return i;
};
int main()
{
    char s1[20],s2[20];
    printf("Unesite prvi string: \n");
    gets(s1);
    printf(" \n Unesite drugi string: \n");
    gets(s2);
    char a = strlen(s1);
    char b = strlen(s2);

    int j= jednaki(a,b);
    if(j==0){
        printf("jednaki su");
    }else(
     printf("Nisu jednaki");     )


    return 0;
}
