#include <iostream>

using namespace std;

int main() {
    int TC, V, E;
    cin >> TC;
    for (int i = 1; i <= TC; ++i) {
        cin >> V >> E;
        cout << E - V + 2 << "\n";
    }
}