#include <stdio.h>
#include <stdlib.h>


    void unos(int* mat){
        int a=0,i,j;
        printf("Unesti elemente matrice \n");
        for(i=0;i<4;i++){
            for(j=0;j<3;j++){
                scanf("%d",(mat+a));
                a+=4;
            }
        printf("\n");
        }
    }

    void ispis(int* mat){
        int a=0,i,j;
        for(i=0;i<4;i++){
            for(j=0;j<3;j++){
                printf("%d",(mat+a));
                a+=4;
            }
        printf("\n");
        }
    }

    void sabiranje(int* mat1,int* mat2){
        int a=0,i,j;
        for(i=0;i<4;i++){
            for(j=0;j<3;j++){
                printf("%d ",*(mat1+a) +  *(mat2+a));
                a+=4;
            }
        printf("\n");
        }
    }



int main(){
    int mat1[4][3];
    int mat2[4][3];
    unos(mat1);
    unos(mat2);
    ispis(mat1);
    ispis(mat2);
    sabiranje(mat1,mat2);
    return 0;
}


