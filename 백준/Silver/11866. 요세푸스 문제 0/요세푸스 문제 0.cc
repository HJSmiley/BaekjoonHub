#include <iostream>
#include <queue>
#include <vector>

using namespace std;

queue<int> q;
vector<int> res;

int main() {
    int n, k, tmp;
    cin >> n >> k;
    int A[n];
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }
    
    while (!q.empty()) {
        for (int i = 1; i < k; i++) {
            q.push(q.front());
            q.pop();
        }
        res.push_back(q.front());
        q.pop();
    }

    cout << '<';
    for (int i = 0; i < res.size(); i++) {
        cout << res[i];
        if (i != res.size() - 1) {
            cout << ", ";
        }
    }
    cout << '>';
}