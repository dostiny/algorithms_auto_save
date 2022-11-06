#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    cout << fixed;
    cout.precision(1);
    for (int i = 0; i < T; ++i) {
        int N, score = 0, total = 0;
        double d1 = 0.0, d2 = 0.0;
        cin >> N;
        for (int j = 0; j < N; ++j) {
            cin >> score >> d1;
            total += score;
            d2 += (d1 * score);
        }
        cout << total << " " << d2 / total << "\n";
    }
    return 0;
}