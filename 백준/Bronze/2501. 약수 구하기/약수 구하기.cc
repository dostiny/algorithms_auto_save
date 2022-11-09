#include <iostream>

using namespace std;

int main() {
    int N, K, cnt = 0, point = 0;
    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        if (N % i == 0) {
            ++cnt;
            if (cnt == K) {
                point = 1;
                cout << i;
                break;
            }
        }
    } if (point == 0) cout << 0;
}