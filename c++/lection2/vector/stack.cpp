#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int main(){
    vector <int> mine;
    mine.push_back(11);
    mine[0] = 111;

    stack <string> first_stack;
    first_stack.push("first");
    first_stack.push("second");
    first_stack.pop();
    cout<<first_stack.top();

}