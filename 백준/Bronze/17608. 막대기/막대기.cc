#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, h;
    stack<int> s;

    cin >> n >> h;
    s.push(h);

    for (int i = 0; i < n - 1; i++) {
        cin >> h;
        
        while (!s.empty() && h > s.top()) {
            s.pop();
        }

        if (s.empty() || s.top() != h) {
            s.push(h);
        }
    }

    cout << s.size();

    return 0;
}