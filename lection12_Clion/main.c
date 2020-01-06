#include <stdio.h>

int main(){
    int arr[3] = {1,2,3};

    printf("%ls\n", &arr[0]);

    printf("%ls\n", &arr[1]);
    return 0;
}