#include <iostream>

using namespace std;

int main() {
    int n, cnt;
    for (int i = 0; i < 3; i++) {
        cnt = 0;
        for (int j = 0; j < 4; j++) {
            cin >> n;
            cnt += n;
        }
        if (cnt == 0) cout << "D" << "\n";
        else if (cnt == 1) cout << "C" << "\n";
        else if (cnt == 2) cout << "B" << "\n";
        else if (cnt == 3) cout << "A" << "\n";
        else if (cnt == 4) cout << "E" << "\n";
    }
}