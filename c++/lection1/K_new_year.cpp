#include <iostream>

using namespace std;

int left(int first,int second){
    while (true){
        if (second < first){
            return 0;
        }else if (second == first)
        {
            return 1;
        }else{
            second-=first;
            first+=first;
        }
        
    }
}
int right(int first,int second){
    while (true){
        if (left(first, second))
        {
            return 1;
        }else if (second > first){
            return 0;
        }else if (second == first)
        {
            return 1;
        }else{
            first-=second;
            second+=second;
        }
        
    }
}

int main(){
    int m,n;
    cin>>m>>n;
    if (right(m, n)|left(m, n)){
        cout<<1;
    }else
    {
        cout<<0;
    }    
    return 0;
}