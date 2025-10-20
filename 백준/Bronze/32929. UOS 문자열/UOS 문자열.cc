#include <iostream>

using namespace std;

int main() {
    int x;
    string s = "SUO";
    
    cin >> x;
    x = x % 3;
    cout << s[x];

    return 0;
}