#include <iostream>

using namespace std;

int main() {
    int n, score, point = 0, sum_n = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> score;
        if (score) {
            point += 1;
            sum_n += point;
        } else point = 0;
    }
    cout << sum_n;
}