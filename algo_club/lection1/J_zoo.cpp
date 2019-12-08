#include <iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int sum = 0;
    for (int i = 2; i < n; i++)
    {
        sum += n-3;
    }
    sum += (n-2)*2;
    cout<<sum;
    return 0;
}