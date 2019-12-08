#include <iostream>
#include <map>

using namespace std;


int main(){
    map<char, char> mapOfWords;

    string layout1, layout2, text, res;  
    cin>>layout1>>layout2>>text;

    for(int i = 0; i < layout1.size(); i++){
        mapOfWords[layout1[i]] = layout2[i];
    }
    for (int i = 0; i < text.size(); i++)
    {
        if (text[i] >= '0' & text[i]<='9')
        {
            res += text[i];
        }
        else if (text[i] < 'a')
        {
            res += mapOfWords[text[i] + 'a'-'A'] - 'a'+'A';
        }
        else{
            res += mapOfWords[text[i]];
        }
    }
    cout<<res<<endl;
}