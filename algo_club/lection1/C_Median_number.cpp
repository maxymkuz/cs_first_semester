#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a;
    int b;
    int c;
    cin>>a>>b>>c;
    int arr[3] = {a, b, c};
    std::sort(arr, arr + 3);
    cout<<arr[1];
}