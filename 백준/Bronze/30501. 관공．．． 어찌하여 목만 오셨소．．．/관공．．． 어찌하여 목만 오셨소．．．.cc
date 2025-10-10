#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string name;
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; i++) {
        getline(cin, name);
        if (name.find("S") != std::string::npos) {
            cout << name;
            break;
        }
    }
    return 0;
}