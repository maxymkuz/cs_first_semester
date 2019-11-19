#include <iostream>
#include <deque>

using namespace std;

int main(){
    deque <int> first_deque;
    cout<<first_deque.empty()<<" "<<first_deque.size()<<endl;
    first_deque.push_back(11);
    first_deque.push_front(98);
    cout<<first_deque.front()<<"  "<<first_deque.back();
}