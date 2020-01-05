#include <stdio.h>

int main(){
    char* arr[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    for (int i = a; i <= b; i++){
        if (i < 10)
            printf("%s", arr[i]);
        else{
        if (i % 2 == 0) printf("even");
        else printf("odd");
        }
        printf("\n");
    }
    return 0;
}