#include <iostream>

using namespace std;

int main(){
    int n,a,b;
    cin>>a>>b>>n;
    a = a*n;
    b = b*n;
    while (b >= 100)    
    {
        b -= 100;
        a++;
    }
    cout<<a<<' '<<b;
    return 0;  
}