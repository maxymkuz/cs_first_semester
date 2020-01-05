#include <stdio.h>
#include <stdlib.h>

int get_int_len(int value){
    int l = 1;
    while(value > 9){
        l++;
        value/=10;
    }
    return l;
}

int power(int a, int b){
    int res = 1;
    for (int i = 0; i < b; ++i) {
        res = res * a;
    }
    return res;
}

int main(){
    int suma, size1, size2;

    printf("Enter size of first array: ");
    scanf("%d", &size1);
    int *arr1;
    arr1 = (int *)malloc(size1 * sizeof(int));
    if(size1 > 0) {
        printf("Now enter %d elements of first array: ", size1);
        for (int i = 0; i < size1; ++i) {
            scanf("%d", &arr1[i]);
        }
    }
    printf("Enter size of second array: ");
    scanf("%d", &size2);

    int *arr2;
    arr2 = (int *)malloc(size2 * sizeof(int));
    if (size2 > 0){
        printf("Now enter %d elements of second array: ", size2);
        for (int i = 0; i < size2; ++i) {
            scanf("%d", &arr2[i]);
        }
    }


    int size = size1 > size2 ? size1 : size2;

    int random[1000000];
    int counter = 0;
    for (int i = 0; i < size; ++i) {
        if (i >= size1) {
            suma = abs(arr2[i]);
        } else if (i >= size2) {
            suma = abs(arr1[i]);
        } else {
            suma = abs(arr1[i] + arr2[i]);
        }

        int length = get_int_len(suma);
        for (int j = 0; suma > 0; ++j) {
            length = get_int_len(suma);
            int p = power(10, length - 1);
            int elem = suma/p;
            suma -= elem*p;
            random[counter] = elem;
            counter++;
        }

    }
    for (int k = 0; k < counter; ++k) {
        printf("%d ", random[k]);
    }
    return 0;
}