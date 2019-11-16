#include <iostream>
#include <algorithm>

using namespace std;

int is_triangle(int k,int m,int n){
    int arr[3] = {k, m, n};
    std::sort(arr, arr + 3);
    if (arr[2] < arr[0]+arr[1]){
        return 1;
    }else if (arr[2] == arr[0]+arr[1]){
        return 2;
    }
    return 0;
}

int main(){
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    int arr[4] = {a,b,c,d};
    bool triangle = false;
    bool segment = false;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (i == j){
                break;
            }
            for (int l = 0; l < 5; l++)
            {
                if (l == j | l==i){
                    break;
                }
                int x = is_triangle(arr[i],arr[j],arr[l]);
                if (x == 1){
                    triangle = true;
                }else if (x ==2){
                    segment = true;
                }
            }   
        }
    }
    if (triangle){
        cout<<"TRIANGLE";
    }else if (segment){
        cout<<"SEGMENT";
    }else
    {
        cout<<"IMPOSSIBLE";
    }
    
    

    return 0;
}