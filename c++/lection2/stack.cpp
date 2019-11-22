#include <iostream>
#include <vector>
#include <stack>
#include <queue>

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

    queue <int> first_queue;
    first_queue.push(11);
    first_queue.push(112);
    first_queue.push(1123);
    while (!first_queue.empty()){
        cout<<first_queue.front()<<" ";
        first_queue.pop();
    }

}