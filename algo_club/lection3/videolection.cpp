#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
 
using namespace std;

// map == dictionary
typedef long long ll;

int main(){
    set<int> s{1, 49, 32, 75, 49, 49};

    set<int>::iterator it = s.end();
    --it;
    cout<<*it<<endl;

    vector<int> v{1, 4, 2, 8, 90, 11};
    sort(v.begin(), v.end());
    cout<<v[5]<<endl;

}