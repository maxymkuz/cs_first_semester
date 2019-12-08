#include <iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int res[n];
    int temp[n];
    for (int i = 0; i < n; i++)
    {
        int temp[n] = {};
        for (int j = 0; j < n-i-1; j++)
        {
            cout<<2<<' ';
            temp[j] = 2;
        }
        cout<<0<<' ';
        temp[n-i] = 0;
        for (int j = 0; j < i; j++)
        {
            cout<<1<<' ';
            temp[j] = 1;
        }
        cout<<endl;
    }
    for (int i = 0; i < n; i++)
    {
        //cout<<temp[i]<<" ";
    }
    
    
    return 0;  
}