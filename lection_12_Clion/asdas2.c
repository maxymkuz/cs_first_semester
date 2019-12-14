#include <stdio.h>

int stepin(int j){
    int res = 1;
    for (int i = 0; i < j; ++i) {
        res *= 10;
    }
    return res;
}


int main(){
    int size1 = 5, size2 = 5,counter = 0;
    int size = size1 > size2 ? size1 : size2;

    int res[100];
    int arr1[5] = {11, 3, 4 , 5, 5};
    int arr2[5] = {1, 3, 4 , 4, 5};

    for (int i = 0; i < size; ++i) {
        if(i < size1){

        }else if(i< size2){

        }else{
            int suma = arr1[i] + arr2[i];
        }


        for (int j = 0; suma > 0; ++j) {
            int elem = suma % stepin(j+1);
            printf("%d \n", elem);
            suma = suma/10;
            res[counter] = elem;
            counter++;
        }

    }
    for (int k = 0; k < counter; ++k) {
        printf("%d ", res[k]);
    }
    return 0;
}