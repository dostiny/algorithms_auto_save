#include <iostream>
using namespace std;

int main() {
    int n, A, B, C;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> A >> B;
        C = A + B;
        cout << "Case #" << i << ": " << A << " + " << B << " = " << C << "\n";
    }
    return 0;
}