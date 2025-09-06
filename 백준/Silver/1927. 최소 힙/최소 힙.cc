#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, tmp;
    cin >> n;

    priority_queue<int> pq;

    for (int i = 0; i < n; i++) {
        cin >> tmp;
        if (tmp != 0) {
            pq.push(-tmp);
        } else if (pq.empty()) {
            cout << 0 << '\n';
        } else {
            cout << -pq.top() << '\n';
            pq.pop();
        }
    }
    
    return 0;
}