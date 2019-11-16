#include <iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    double temp;
    int num_of_glass = 0;
    int packages = 0;
    for (int i = 0; i < n; i++)
    {
        cin>>temp;
        if(temp < 30){
        num_of_glass++;
        packages += 200;
        }
    }
    double ans = packages / 900;
    if (packages % 900 != 0){
        ans++;
    }
    cout<<ans<<" "<<num_of_glass;
    return 0;
}

