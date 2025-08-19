#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int D[n + 1];
    D[0] = 0;
    D[1] = 1;
    for (int i = 2; i < n + 1; i++) {
        D[i] = D[i-1] + D[i-2];
    }

    cout << D[n];
}