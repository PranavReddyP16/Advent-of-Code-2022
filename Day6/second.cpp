#include<bits/stdc++.h>
using namespace std;

int check(map<char, int> &count) {
    int distinct=0;
    for(pair<char, int> letter : count) {
        if(letter.second>0) {
            distinct++;
        }
    }

    return distinct;
}

int main() {
    ifstream input_file;
    input_file.open("input.txt");

    string input;
    input_file>>input;

    map<char, int> count;
    for(int i=0;i<14;i++) {
        count[input[i]]++;
    }

    for(int i=14;i<(int)input.size();i++) {
        count[input[i]]++;
        count[input[i-14]]--;
        if(check(count) == 14) {
            cout<<i+1<<endl;
            return 0;
        }
    }
}