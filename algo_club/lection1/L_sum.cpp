#include <iostream>

using namespace std;

int sum_of_digits(int number){
    int res = 0;
    while (number > 0)
    {
        res += number%10;
        number /= 10;
    }
    return res;
    
}

int main(){
    int n;
    int ans = 0;
    cin>>n;
    for (int i = 10; i < 100; i++)
    {
        if (sum_of_digits(i) == sum_of_digits(n*i)){
            ans++;
        }
    }
    cout<<ans;
    return 0;
}