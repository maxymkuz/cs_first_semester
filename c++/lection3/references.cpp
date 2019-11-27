#include <iostream>

using namespace std;

// ALWAYS pass containers by REFERENCE
// ALWAYS pass things by const reference if you are not going to modify it inside the function

int main(){
    int a = 11;
    int &copy = a;
    cout<<a<<" "<<copy<<endl;
    a = 1245;
    cout<<a<<" "<<copy<<endl;
}