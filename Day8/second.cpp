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

vector<int> get_visible_values_for_array(vector<int> arr) {
    int len = arr.size();
    vector<int> max_till_here(len), max_from_here(len);

    int mx_idx=0;
    for(int i=1;i<len;i++) {
        if(arr[i] <= arr[mx_idx]) {
            max_till_here[i] = i - mx_idx;
        }
        else {
            max_till_here[i] = i;
        }
        if(arr[mx_idx] <= arr[i]) {
            mx_idx = i;
        }
    }

    mx_idx = len-1;
    for(int i=len-2;i>=0;i--) {
        if(arr[i] <= arr[mx_idx]) {
            max_from_here[i] = mx_idx - i;
        }
        else {
            max_from_here[i] = len - 1 - i;
        }
        if(arr[mx_idx] <= arr[i]) {
            mx_idx = i;
        }
    }

    vector<int> ans(len);
    for(int i=0;i<len;i++) {
        ans[i] = max_till_here[i]*max_from_here[i];
    }

    return ans;
}

int main() {
    vector<vector<int>> trees = handle_input();
    int n = trees.size();
    int m = trees[0].size();

    int ans=0;
    for(int i=1;i<n-1;i++) {
        for(int j=1;j<m-1;j++) {
            int k = j-1;
            int left=1;
            while(trees[i][k] < trees[i][j]) {
                k--;
                if(k<0) break;
                left++;
            }

            k=j+1;
            int right = 1;
            while(trees[i][k] < trees[i][j]) {
                k++;

                if(k==n) break;
                right++;
            }

            k = i-1;
            int up=1;
            while(trees[k][j] < trees[i][j]) {
                k--;

                if(k<0) break;
                up++;
            }

            k = i+1;
            int down=1;
            while(trees[k][j] < trees[i][j]) {
                k++;

                if(k==n) break;
                down++;
            }

            ans = max(ans, up*down*left*right);
            // cout<<i<<" "<<j<<": "<<up<<" "<<down<<" "<<left<<" "<<right<<endl;
        }
    }

    cout<<ans<<endl;
}