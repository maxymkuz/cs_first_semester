#include <stdio.h>
#include <string.h>

int main(){
    int height;
    char* str[10];


    while(1 > 0){
        printf("enter height: ");
        char input[100];
        scanf("%s", input);
        int length = strlen(input);

        if(length > 2 || length == 0 || input[0] > '9' || input[0] < '0'){
            continue;
        }
        if(length == 2){
            if(input[1] > '9' || input[1] < '0')
                continue;
        }
        sscanf(input, "%d", &height);

        if(height<=24)
            break;

        }

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