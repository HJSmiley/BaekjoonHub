#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string str;
    while (true) {
        getline(cin, str);
        if (str == ".") break;

        stack<char> s;
        bool isBalanced = true;

        for (char ch : str) {
            if (ch == '(' || ch == '[') {
                s.push(ch);
            } else if (ch == ')') {
                if (s.empty() || s.top() != '(') {
                    isBalanced = false;
                    break;
                }
                s.pop();
            } else if (ch == ']') {
                if (s.empty() || s.top() != '[') {
                    isBalanced = false;
                    break;
                }
                s.pop();
            }
        }

        if (!s.empty()) isBalanced = false;

        if (isBalanced) cout << "yes" << endl;
        else cout << "no" << endl;
    }
    
    return 0;
}