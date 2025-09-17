#include <iostream>
#include <math.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int n, sum;
    cin >> n;

    sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    cout << sum << '\n';
    cout << int(pow(sum, 2)) << '\n';

    sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += pow(i, 3);
    }
    cout << sum << '\n';
}