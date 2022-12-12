#include<bits/stdc++.h>
using namespace std;

bool check(char x, char y);

vector<pair<int, int>> get_adj(const vector<string> &grid, pair<int, int> pos) {
    int n = grid.size();
    int m = grid[0].size();

    vector<pair<int, int>> adj;
    if(pos.first+1 < n && check(grid[pos.first][pos.second], grid[pos.first+1][pos.second])) {
        adj.push_back({pos.first+1, pos.second});
    }
    if(pos.first-1 >= 0 && check(grid[pos.first][pos.second], grid[pos.first-1][pos.second])){
        adj.push_back({pos.first-1, pos.second});
    }
    if(pos.second+1 < m && check(grid[pos.first][pos.second], grid[pos.first][pos.second+1])){
        adj.push_back({pos.first, pos.second+1});
    }
    if(pos.second-1 >= 0 && check(grid[pos.first][pos.second], grid[pos.first][pos.second-1])){
        adj.push_back({pos.first, pos.second-1});
    }

    return adj;
}

bool check(char x, char y) {
    return x-y < 2;
}

int bfs(vector<string> &grid, pair<int, int> start) {
    int n = grid.size();
    int m = grid[0].size();

    vector<vector<int>> dist(n, vector<int> (m, 1e9+1));
    vector<vector<int>> vis(n, vector<int> (m));

    queue<pair<int, int>> q;
    q.push(start);
    dist[start.first][start.second] = 0;
    while(!q.empty()) {
        pair<int, int> u = q.front();
        q.pop();
        for(pair<int, int> v : get_adj(grid, u)) {
            if(vis[v.first][v.second]) continue;

            dist[v.first][v.second] = dist[u.first][u.second]+1;
            vis[v.first][v.second] = 1;
            q.push(v);
        }
    }

    int mn = 1e9+1;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(grid[i][j]=='a') mn = min(mn, dist[i][j]);
        }
    }

    return mn;
}

int main() {
    ifstream input_file;
    input_file.open("input.txt");
    // input_file.open("test_input.txt");

    int n = 41;
    // int n = 5;
    vector<string> grid(n);
    for(int i=0;i<n;i++) {
        input_file>>grid[i];
    }
    int m = grid[0].size();

    pair<int, int> start;
    pair<int, int> end;

    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(grid[i][j] == 'S') {
                start = {i, j};
                grid[i][j] = 'a';
            }
            if(grid[i][j] == 'E') {
                end = {i, j};
                grid[i][j] = 'z';
            }
        }
    }

    cout<<bfs(grid, end)<<endl;
}