#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    string mine;
    string second = "to swap";
    if (mine.empty()){
        mine += "was empty";
        mine.push_back('A');
        mine.swap(second);
        mine.erase(0, 1);
    }
    cout<<mine;
    return 0;
}