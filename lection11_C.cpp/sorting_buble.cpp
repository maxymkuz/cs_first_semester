#include <iostream>
#include <array>

#include <bits/stdc++.h> 
using namespace std; 

int main(){
    int arr[10];
    int temp;
    for (int i = 0; i < 10; i++)
    {
        cin>>arr[i];
    }
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        for (int x = 0; x < 10; x++){
            cout<<arr[x]<<" ";
        }
        cout<<endl;
    }

}