#include <iostream>

using namespace std;

int main(){
    int n,m,x,y;
    cin>>n>>m>>x>>y;//m-rpw   n-column
    int ans;
    ans = (x-1)*m - 1;
    if (x%2 == 1){
        for (int i = 1; i <= y; i++)//even row
        {
            ans++;
        }
    }
    else
    {
        for (int i = y; i <= m; i++)
        {
            ans++;
        }
        
    }
    cout<<ans;
    return 0;
}