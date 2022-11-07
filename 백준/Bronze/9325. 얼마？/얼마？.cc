#include <iostream>

using namespace std;

int main() {
    int TC, car, n, m, pay;
    cin >> TC;
    for (int i = 0; i < TC; ++i) {
        cin >> car;
        cin >> n;
        for (int j = 0; j < n; ++j) {
            cin >> m >> pay;
            car += m * pay;
        }
        cout << car << "\n";
    }
    return 0;
}