#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    string key;
    map<string, int> dic;
    vector<string> ans;

    for (int i = 0; i < n; i++) {
        cin >> key;
        if (dic.count(key)) {
            dic[key] += 1;
        } else {
            dic[key] = 0;
        }
    }

    for (int i = 0; i < m; i++) {
        cin >> key;
        if (dic.count(key)) {
            ans.push_back(key);
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << endl;
    }

    return 0;
}