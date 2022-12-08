#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> handle_input() {
    ifstream input_file;
    input_file.open("nice_input.txt");

    int n,m;
    input_file>>n;

    vector<string> input(n);
    for(int i=0;i<n;i++) {
        input_file>>input[i];
    }

    m = input[0].size();

    vector<vector<int>> trees(n, vector<int> (m));
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            trees[i][j] = (int)(input[i][j] - '0');
        }
    }
    
    return trees;
}

vector<int> get_visible_positions_for_array(vector<int> arr) {
    int len = arr.size();
    vector<int> max_till_here(len, -1), max_from_here(len, -1);

    int mx=arr[0];
    for(int i=1;i<len;i++) {
        max_till_here[i] = mx;
        mx = max(mx, arr[i]);
    }

    mx = arr[len-1];
    for(int i=len-2;i>=0;i--) {
        max_from_here[i] = mx;
        mx = max(mx, arr[i]);
    }

    vector<int> ans;
    for(int i=0;i<len;i++) {
        if(!(max_till_here[i] >= arr[i] && max_from_here[i] >= arr[i])) {
            ans.push_back(i);
        }
    }

    return ans;
}

int main() {
    vector<vector<int>> trees = handle_input();
    int n = trees.size();
    int m = trees[0].size();

    vector<vector<int>> visible(n, vector<int> (m));

    // Rows first
    for(int i=0;i<n;i++) {
        vector<int> visible_positions = get_visible_positions_for_array(trees[i]);
        for(int position : visible_positions) {
            visible[i][position]++;
        }
    }

    // Columns
    for(int j=0;j<m;j++) {
        vector<int> column(n);
        for(int i=0;i<n;i++) {
            column[i] = trees[i][j];
        }

        vector<int> visible_positions = get_visible_positions_for_array(column);
        for(int position : visible_positions) {
            visible[position][j]++;
        }
    }

    int ans=0;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(visible[i][j] > 0) {
                ans++;
            }
        }
    }

    cout<<ans<<endl;
}