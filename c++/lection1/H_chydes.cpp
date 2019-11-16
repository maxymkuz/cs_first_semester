#include <iostream>

using namespace std;

int main(){
    int main[26];
    string ipt;
    int num;
    int counter = 0;
    cin>>ipt;
    for (int i = 0; i < 26; i++)
    {
        main[i] = 0;
    }
    
    for (int i = 0; i < ipt.length(); i++)
    {
        num = int(ipt[i]) - 65;
        main[num] = 1;
    }
    for (int i = 0; i < 26; i++)
    {
        counter += main[i];
    }
    cout<<counter;
    return 0;
}