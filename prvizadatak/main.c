#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, j;
    int Matrica[100][100], t[100][100];
    printf("Unesite dimenziju kvadratne matrice:  \n");
    scanf("%d", &n);

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("Unesite element matrice[%d][%d]", i, j);
            scanf("%d", &Matrica[i][j]);

        }
    }
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            t[j][i] = Matrica[i][j];
        }
    }

    printf("Transponovana matrica:\n");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ", t[i][j]);
        }
        printf("\n");
    }
    return 0;
}
