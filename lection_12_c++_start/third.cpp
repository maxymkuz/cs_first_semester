#include <stdio.h>

using namespace std;
#import <string>

int main(){
    char* arr[40];
    int counter = 0;
    // while (counter < 4){
    //     scanf("%s", arr[counter]);
    //     counter++;
    // }
    std::string str(100, ' ');
    if (1 == scanf("%*s", &str[0], str.size())) {
        printf("")
    }
    printf("%s _____ ", str);
    return 0;
}