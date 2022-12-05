#include<bits/stdc++.h>
using namespace std;
int main() {
    ifstream input;
    input.open(".\\nice_input.txt");

    int num_stacks;
    input>>num_stacks;

    vector<stack<char>> stack_list(num_stacks);
    for(int i=0;i<num_stacks;i++) {
        int stack_size;
        input>>stack_size;

        stack<char> cur_stack;
        for(int j=0;j<stack_size;j++) {
            char element;
            input>>element;
            cur_stack.push(element);
        }

        stack_list[i] = cur_stack;
    }

    int num_moves;
    input>>num_moves;

    for(int i=0;i<num_moves;i++) {
        int boxes_moved, from, to;
        input>>boxes_moved>>from>>to;
        from--, to--;

        stack<char> transfer_stack;
        for(int j=0;j<boxes_moved;j++) {
            char moved_element = stack_list[from].top();
            stack_list[from].pop();
            transfer_stack.push(moved_element);
        }

        while(!transfer_stack.empty()) {
            char moved_element = transfer_stack.top();
            stack_list[to].push(moved_element);
            transfer_stack.pop();
        }
    }

    string ans="";

    for(int i=0;i<num_stacks;i++) {
        ans.push_back(stack_list[i].top());
    }
    cout<<ans<<endl;
}