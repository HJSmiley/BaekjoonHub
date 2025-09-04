#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;

        queue<pair<int, int>> q;
        priority_queue<int> pq;

        for (int j = 0; j < n; j++){
            int tmp;
            cin >> tmp;
            q.push({tmp, j});
            pq.push(tmp);
        }

        int count = 0;

        while (!q.empty()){
            int cur = q.front().first;
            int idx = q.front().second;
            if (cur == pq.top()) {
                count++;
                if(idx == m){
                    cout << count << "\n";
                    break;
                }
                q.pop();
                pq.pop();
            } else {
                q.push(q.front());
                q.pop();
            }
        }
    }

    return 0;
}