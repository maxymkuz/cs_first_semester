#include <iostream>

using namespace std;

int main(){
    long long inpt;
    int len = 0;
    int res = 0;
    cin>>inpt;
    long long n = inpt;
    while(inpt > 0){
        len++;
        inpt /= 10;
    }
    int num_array[len];
    for(int i = 0; i < len; i++){
        num_array[i] = n%10;
        n /= 10;

    }
    for (int i = 0; i < len / 2 + 1; i++)
    {
        if (num_array[i] == num_array[len - i - 1]){
            res++;
        }
    }
    cout<<res;
    return 0;
}