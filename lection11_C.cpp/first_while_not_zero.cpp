/*
читати поки не нуль
вивести скільки парнихскільки додатних найбільше, найменше 0 просто кінець вводу

2) Читати масив з 10 елементів і сортувати
*/

#include <iostream>

using namespace std;

int main(){
    int counter = 0, sum = 0, num_of_even = 0, num_of_positive = 0;
    int min_elem, max_elem;
    while(true){
        int temp;
        cin>>temp;

        if (temp == 0)
        {
            break;
        }

        if (counter == 0){
            max_elem = temp;
            min_elem = temp;
            counter++;
        }
        else{
            counter++;
            if (temp > max_elem){
            max_elem = temp;
            }
            if (temp < min_elem){
                min_elem = temp;
            }
        }
        
        if(temp%2 == 0){
            num_of_even++;
        }
        if(temp>0){
            num_of_positive++;
        }
        sum += temp;
        
    }
    cout<<counter<<" "<<num_of_even<<" "<<num_of_positive<<" "<<sum<<" "<<max_elem<<" "<<min_elem<<endl;
}


