#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<ll, ll>
#define fi first
#define se second

struct WaterBottle
{
    int x, y;
    vector<pi> path;
};

void bfs(WaterBottle s, int x, int y, int z){
    queue<WaterBottle> q;
    q.push(s);
    map<pi, int> visited;
    visited[{s.x, s.y}] = 1;
    while (!q.empty()){
        WaterBottle u = q.front();
        q.pop();
        if (u.x==z && u.y==0){
            u.path.push_back({u.x, 0});
            for (auto x: u.path){
                cout << x.fi << " " << x.se << "\n";
            }
            return;
        }
        if (u.x==0 && u.y==z){
            u.path.push_back({0, u.y});
            for (auto x: u.path){
                cout << x.fi << " " << x.se << "\n";
            }
            return;
        }
        vector<WaterBottle> next_state;
        next_state.push_back({u.x+min(u.y, x-u.x), u.y-min(u.y, x-u.x), u.path});
        next_state.push_back({u.x-min(u.x, y-u.y), u.y+min(u.x, y-u.y), u.path});
        next_state.push_back({x, u.y, u.path});
        next_state.push_back({u.x, y, u.path});
        next_state.push_back({0, u.y, u.path});
        next_state.push_back({u.x, 0, u.path});
        for (auto v: next_state){
            if (!visited[{v.x, v.y}]) {
                visited[{v.x, v.y}] = 1;
                v.path.push_back({u.x, u.y});
                q.push(v);
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int x, y, z;
    cin >> x >> y >> z;
    bfs({0, 0}, x, y, z);
    return 0;
}
/*
7 5 4
*/
