#include <stdio.h>
#include <string.h>


int get_square_floor(int a){
    int res = 0;
    while((res+1)*(res+1) <= a){
        res++;
    }
//    printf("rs: %d\n", res);
    return res;
}


int main(){
    char starting_string[82];
    char no_spaces[82];
    int counter = 0;
    scanf ("%[^\n]%*c", starting_string);

    for(int i = 0; i < strlen(starting_string); i++){
        if(starting_string[i] != ' '){
            no_spaces[counter] = starting_string[i];
            counter++;
        }
    }

    int floor = get_square_floor(counter);
    int rows = floor, columns;
    if(rows*rows >= counter)
        columns = rows;
    else if (rows*(rows+1) >= counter)
        columns = rows + 1;
    else{
        rows++;
        columns = rows;
    }

//    printf("%d \n", rows);
//    printf("%d \n", columns);
//    printf("counter %d\n", counter);

    int letter = 0;
    for (int j = 0; j < rows; ++j) {
        for (int i = 0; i < columns; ++i) {
            if(letter == counter){
                break;
            }
            printf("%c", no_spaces[letter]);
            letter++;
        }
        printf("\n");
    }
    return 0;
}