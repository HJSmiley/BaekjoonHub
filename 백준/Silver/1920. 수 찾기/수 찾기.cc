#include <stdio.h>
#include <set>

using namespace std;

int main() {
    int n, m, num;
    set<int> s;

    scanf("%d", &n);
    int A[n];
    for(int i = 0; i < n; i++) {
        scanf("%d", &num);
        s.insert(num);
    }

    scanf("%d", &m);
    int B[m];
    for(int i = 0; i < m; i++) {
        scanf("%d", &B[i]);
    }

    for(int i = 0; i < m; i++) {
        if (s.find(B[i]) != s.end()) {
            printf("1\n");
        } else {
            printf("0\n");
        }
    }
    
    return 0;
}