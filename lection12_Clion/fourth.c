#include <stdio.h>

int main(){
    double num;
    int res = 0;

    while(1 > 0) {
        printf("Enter num");
        scanf("%lf", &num);
        num *= 100;
        if(num == (int)num && num >= 0){
            num = (int)num;
            break;
        }
    }

    int coins[4] = {25,10,5,1};
    for (int i = 0; i < 4; ++i) {
        while(num >= coins[i]){
            num -= coins[i];
            res++;
        }
    }
    printf("Result: %d", res);
    return 0;
}