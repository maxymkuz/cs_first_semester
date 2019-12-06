#include <stdio.h>

int main(){
    int height;
    scanf("%d", &height);
    for (int i = 2; i < height + 2; i++){
        for (int j = 0; j < height-i + 1; j++)
        {
            printf(" ");
        }
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}