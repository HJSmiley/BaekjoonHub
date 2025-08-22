#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    stack<int> s;
    vector<char> res;

    int x, curr = 1;
    for (int i = 0; i < n; i++) {
        cin >> x;

        while (curr <= x) {
            s.push(curr++);
            res.push_back('+');
        }

        if (s.top() == x) {
            s.pop();
            res.push_back('-');
        } else {
            cout << "NO\n";
            return 0;
        }
    }

    for (char c : res) {
        cout << c << '\n';
    }
    return 0;
}