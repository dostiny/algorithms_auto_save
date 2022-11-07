#include <iostream>

using namespace std;

int main() {
    int TC, c, v;
    cin >> TC;
    for (int i = 0; i < TC; ++i) {
        cin >> c >> v;
        cout << "You get " << c / v << " piece(s) and your dad gets " << c % v << " piece(s)." << "\n";
    }
}