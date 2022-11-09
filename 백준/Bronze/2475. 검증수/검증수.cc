#include <iostream>

using namespace std;

int main() {
    int n, num = 0, last;
    for (int i = 0; i < 5; i++ ) {
        cin >> n;
        num += (n * n);
    }
    last = num % 10;
    cout << last;
}