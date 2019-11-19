#include <iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int differance [n];
    int sum = 0;
    int max_possible = 0;
    int k = 0;
    int x;
    int y;
    for (int i = 0; i < n; i++){
        cin>>x>>y;
        differance[i] = x - y;
        sum += x - y;
    }
    max_possible = abs(sum);
    for (int i = 0; i < n; i++)
    {
        // cout<<max_possible<<" "<<i<<endl;
        if (abs(sum - 2*differance[i]) > max_possible)
        {
            max_possible = (abs(sum - 2*differance[i]));
            k = i + 1;
        }
    }
    // cout<<sum<<endl;
    // cout<<max_possible<<endl;
    cout<<k;    
}