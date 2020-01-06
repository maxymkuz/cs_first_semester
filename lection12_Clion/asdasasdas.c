#include <stdio.h>


double ser_aryfm(double a, double b){
    return (a+b)/2;
}

void larger_change(double* arr1, double* arr2, int size){
    for (int i = 0; i < size; ++i) {
        double ser = ser_aryfm(arr1[i], arr2[i]);
        if (arr1[i] > arr2[i]){
            arr1[i] = ser;
        } else if(arr1[i] < arr2[i]){
            arr2[i] = ser;
        } else{
            arr2[i] = ser;
            arr1[i] = ser;
        }
    }
}


int main(){
    printf("enter the size of both arrays: ");
    int size;
    scanf("%d", &size);
    double *arr1;
    arr1 = (double *)malloc(size * sizeof(double));
    printf("Now enter %d elements of first array", size);
    for (int i = 0; i < size; ++i) {
        scanf("%lf", &arr1[i]);
    }
    printf("Now enter %d elements of second array", size);
    double *arr2;
    arr2 = (double *)malloc(size * sizeof(double));
    for (int i = 0; i < size; ++i) {
        scanf("%lf", &arr2[i]);
    }
    larger_change(arr1, arr2, size);
    for (int i = 0; i < size; ++i) {
        printf("%lf ", arr1[i]);
    }
    printf("\n");
    for (int i = 0; i < size; ++i) {
        printf("%lf ", arr2[i]);
    }
    return 0;
}