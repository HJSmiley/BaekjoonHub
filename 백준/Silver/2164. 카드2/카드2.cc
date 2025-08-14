#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;

    queue<int> q;
    for (int i = 1; i < n+1; i++) {
        q.push(i);
    }

    int res = q.back();
    while (!q.empty()) {
        // 제일 위에 있는 카드를 바닥에 버린다
        q.pop();
        res = q.back();

        // 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
        if (!q.empty()) {
            q.push(q.front());
            q.pop();
            res = q.back();
        }
    }

    cout << res;

    return 0;
}