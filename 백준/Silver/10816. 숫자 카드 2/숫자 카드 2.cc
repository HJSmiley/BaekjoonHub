#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m, tmp;
    cin >> n;
    
    int arr[n + 1];
    for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr[i] = tmp;
	}
    sort(arr, arr + n);

    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> tmp;
        cout << upper_bound(arr, arr + n, tmp) - lower_bound(arr, arr + n, tmp) << ' ';
    }

    return 0;
}