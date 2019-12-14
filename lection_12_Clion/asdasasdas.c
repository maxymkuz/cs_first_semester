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
    int size;
    scanf("%d", size);

    double arr1[7] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0};
    double arr2[7] = {7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0};
    larger_change(arr1, arr2, size);
    for (int i = 0; i < size; ++i) {
        printf("%f ", arr1[i]);
    }
    printf("\n");
    for (int i = 0; i < size; ++i) {
        printf("%f ", arr2[i]);
    }
    return 0;
}